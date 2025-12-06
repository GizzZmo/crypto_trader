# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to the project maintainers. You should receive a response within 48 hours. If for some reason you do not, please follow up to ensure we received your original message.

### What to Include in Your Report

Please include the following information:

- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Process

1. **Acknowledgment**: We will acknowledge your email within 48 hours
2. **Investigation**: We will investigate and validate the vulnerability
3. **Fix Development**: We will work on a fix for the issue
4. **Release**: We will release a patched version
5. **Disclosure**: We will publicly disclose the vulnerability after the patch is released

## Security Best Practices for Users

### API Key Protection

1. **Never commit API keys to version control**
   - Use environment variables
   - Use configuration files (add to .gitignore)
   - Consider using a secrets manager

2. **Restrict API Key Permissions**
   - Only enable necessary permissions (e.g., spot trading only)
   - Never enable withdrawal permissions for trading bots
   - Use IP whitelisting when possible

3. **Rotate Keys Regularly**
   - Change API keys periodically
   - Immediately rotate if compromised

### Safe Trading Practices

1. **Start with Testnet**
   - Always test with demo mode first
   - Verify bot behavior before live trading
   - Test with small amounts initially

2. **Monitor Regularly**
   - Check bot activity frequently
   - Set up alerts for unusual activity
   - Review trade history regularly

3. **Risk Management**
   - Never invest more than you can afford to lose
   - Set appropriate investment limits
   - Use stop-loss mechanisms when available

### Application Security

1. **Keep Dependencies Updated**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Run in Isolated Environment**
   - Use virtual environments
   - Consider containerization (Docker)
   - Limit network access if possible

3. **Secure Configuration**
   - Don't share configuration files with credentials
   - Use strong passwords for any authentication
   - Enable two-factor authentication on exchange accounts

### Network Security

1. **Use Secure Connections**
   - Ensure HTTPS/WSS connections to exchanges
   - Verify SSL certificates
   - Use VPN when on public networks

2. **Firewall Configuration**
   - Limit outbound connections to necessary endpoints
   - Block unnecessary inbound connections
   - Monitor network traffic for anomalies

## Known Security Considerations

### API Credentials Storage

- **Current**: API credentials are stored in memory during runtime
- **Risk**: Credentials could be exposed if application crashes with core dump
- **Mitigation**: 
  - Don't run on untrusted systems
  - Use testnet for development
  - Consider using hardware security modules for production

### GUI Input Validation

- **Current**: Basic input validation on form fields
- **Enhancement Planned**: More robust validation in future versions
- **Mitigation**: 
  - Verify all inputs before trading
  - Start with small amounts
  - Monitor bot behavior

### Third-Party Dependencies

- **Current**: Relies on several third-party libraries
- **Risk**: Vulnerabilities in dependencies could affect the bot
- **Mitigation**:
  - We monitor dependencies for known vulnerabilities
  - Update dependencies regularly
  - Use tools like `safety` to check for known issues:
    ```bash
    pip install safety
    safety check -r requirements.txt
    ```

## Security Checklist for Contributors

When contributing code, ensure:

- [ ] No hardcoded credentials or secrets
- [ ] Input validation for all user inputs
- [ ] Proper error handling (no information leakage)
- [ ] Secure API communication (HTTPS/WSS)
- [ ] No SQL injection vulnerabilities (if using databases)
- [ ] No command injection vulnerabilities
- [ ] Proper authentication and authorization
- [ ] Secure random number generation (for cryptographic operations)
- [ ] No sensitive data in logs
- [ ] Dependencies are up-to-date and vetted

## Vulnerability Disclosure Timeline

We aim to:

1. **48 hours**: Acknowledge receipt of vulnerability report
2. **7 days**: Provide initial assessment and timeline
3. **30 days**: Release patch (for critical vulnerabilities)
4. **90 days**: Public disclosure (after patch release)

This timeline may be adjusted based on:
- Severity of the vulnerability
- Complexity of the fix
- Coordination with other affected parties

## Security Updates

Security updates will be:

- Released as soon as possible
- Clearly marked in release notes
- Announced through GitHub Security Advisories
- Documented in CHANGELOG.md

## Acknowledgments

We appreciate the security research community's efforts in responsibly disclosing vulnerabilities. Contributors who report valid security issues will be:

- Credited in the security advisory (if desired)
- Listed in our CONTRIBUTORS.md
- Mentioned in release notes

Thank you for helping keep this project and its users safe!

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Binance API Security](https://www.binance.com/en/support/faq/360002502072)

---

**Last Updated**: December 2025
