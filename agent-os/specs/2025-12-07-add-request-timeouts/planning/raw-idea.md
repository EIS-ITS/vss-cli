# Raw Idea: Add Request Timeouts Security Fix

## Feature Description

Address Bandit B113 security issues - adding timeout parameters to all `requests` library calls that are currently missing them.

The following files and lines need to be fixed:
- vss_cli/config.py:1901 - Call to requests without timeout
- vss_cli/config.py:1919 - Call to requests without timeout
- vss_cli/config.py:1972 - Call to requests without timeout
- vss_cli/config.py:2154 - Call to requests without timeout
- vss_cli/hcio.py:17 - Call to requests without timeout
- vss_cli/sstatus.py:25 - Call to requests without timeout
- vss_cli/sstatus.py:49 - Call to requests without timeout

This is a security fix to prevent requests from hanging indefinitely by adding appropriate timeout values.
