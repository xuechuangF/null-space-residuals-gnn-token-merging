"""Submit this GitHub Pages URL after its IndexNow key file is published."""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PAGES_URL = "https://xuechuangf.github.io/null-space-residuals-gnn-token-merging/"
HOST = "xuechuangf.github.io"
ENDPOINT = "https://api.indexnow.org/indexnow"


def payload_for(key):
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", key):
        raise ValueError("Key must contain 8-128 ASCII letters, digits, or hyphens.")
    return {
        "host": HOST,
        "key": key,
        "keyLocation": PAGES_URL + key + ".txt",
        "urlList": [PAGES_URL],
    }


def read_response(request):
    try:
        with urlopen(request, timeout=30) as response:
            return response.status, response.read()
    except HTTPError as error:
        return error.code, error.read()


def print_response(status, body):
    print("HTTP status code:", status)
    print("Response content:")
    print(body.decode("utf-8", errors="replace") if body else "(empty)")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--key", required=True, help="IndexNow key matching the published <KEY>.txt")
    parser.add_argument("--dry-run", action="store_true", help="Print the request without any network calls")
    args = parser.parse_args(argv)
    try:
        payload = payload_for(args.key)
        if args.dry_run:
            print("POST", ENDPOINT)
            print(json.dumps(payload, indent=2))
            return 0
        key_file = Path(__file__).resolve().parent / (args.key + ".txt")
        expected = args.key.encode("utf-8")
        if key_file.read_bytes() != expected:
            raise ValueError("Local key file must contain exactly the key, with no other bytes.")
        check = Request(payload["keyLocation"], headers={"User-Agent": "NSR-IndexNow-Submitter/1.0", "Cache-Control": "no-cache"})
        status, body = read_response(check)
        print("Published key file HTTP status code:", status)
        if status != 200 or body != expected:
            print("Key file is not published with the expected content. No IndexNow submission was sent.")
            print_response(status, body)
            return 1
        request = Request(
            ENDPOINT, data=json.dumps(payload).encode("utf-8"), method="POST",
            headers={"Content-Type": "application/json; charset=utf-8", "Accept": "application/json", "User-Agent": "NSR-IndexNow-Submitter/1.0"},
        )
        status, body = read_response(request)
        print_response(status, body)
        if status == 200:
            print("Submission received. Search indexing is not guaranteed.")
        elif status == 202:
            print("Submission received; IndexNow key validation is pending.")
        return 0 if status in (200, 202) else 1
    except (ValueError, OSError, URLError) as error:
        print("Error:", error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
