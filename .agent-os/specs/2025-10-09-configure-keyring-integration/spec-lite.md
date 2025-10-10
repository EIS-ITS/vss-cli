# Spec Summary (Lite)

Update `vss-cli configure ls` and `configure mk` commands to integrate with the secure credential backend system (Keychain, 1Password, encrypted file). The `ls` command will retrieve and display usernames from credential backends instead of parsing base64 auth fields, while `mk` will automatically store new credentials in the most secure available backend. Legacy base64 credentials will continue to work during the transition period.
