# Code tour

This hidden directory contains teaching metadata for websites and other guided views of the
example. It does not duplicate example code.

`code-tour.json` uses the version 2 tour format:

- `entries` is an ordered list of teaching topics. A tour may contain any number of entries.
- Each entry contains one or more `sources`. Multiple sources are displayed together as one
  explained code section in the listed order.
- `link` belongs to the complete tour. Consumers display this required link once in the footer
  after all entries, rather than repeating documentation links for every entry.

Each source points to a code construct using a semantic selector:

- `python-assignment` extracts the complete assignment with the given name.
- `python-function` extracts the complete function; `includeDecorators` also includes its
  decorators.

Each selector must match exactly one source construct. A consuming build should fail when a
selector is missing or ambiguous, making source changes that need tutorial updates visible.

Explanations and the shared footer link are versioned here because they are teaching content
specific to this example. Consumers present entries and their sources in manifest order.
