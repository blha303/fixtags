#!/usr/bin/env python3
import mutagen
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--title")
    parser.add_argument("-a", "--artist")
    parser.add_argument("-A", "--album")
    parser.add_argument("track")
    args = parser.parse_args()
    if not any((args.title, args.artist, args.album)):
        print("Specify one of --track, --artist, --album", file=sys.stderr)
        return 1
    track = mutagen.File(args.track, easy=True)
    if args.title:
        track["title"] = args.title
    if args.artist:
        track["artist"] = args.artist
    if args.album:
        track["album"] = args.album
    track.save()
    return 0

if __name__ == "__main__":
    sys.exit(main())
