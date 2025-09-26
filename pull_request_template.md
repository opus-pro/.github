## Summary

_❗️❗️❗️Please include a summary of the change❗️❗️❗️_

1. **Why**: Why you create this Pull Request? What's the situation before this Pull Request?
2. **How**: Is this Pull Request single purpose? How do you plan this PR overall?
3. **What**: What's the most important change in this PR? How to describe the change in one sentence? (That should be the title)

## Checklist

> General guidelines of code changes.

- [ ] Control large/key change in [Statsig](https://console.statsig.com/).

## Tests

> How is the changed tested?

- [ ] Manually tested or added unit test

## Screenshots/GIFs

> snapshots or gifs (if interaction is the majority of the change)

- [ ] Added screenshots or this feature doesn't involve any UI change

## Tips for code reviews

### Complexity

> Could the code be made simpler? Would another developer be able to easily understand and use this code when they come across it in the future?

- Added technical design documentation if it is complex.

### Security

> Are there any security risks in the code as identified by the latest OWASP Top 10?

- Injection attacks
- Broken access control
- Sensitive data exposure
- Cross-site scripting (XSS)
- Broken authentication
- Security misconfigurations
- Vulnerable components
- Insufficient logging and monitoring
- Cross-site request forgery (CSRF)
- Server-side request forgery (SSRF)

### Naming

> Are there clear names for variables, classes, methods, etc.?

- Ensure have checked the naming standard. [go/naming](https://opusclip.larksuite.com/wiki/CG2LwVKS2ivHC3k1weeubLa7sgq)

### Comments

> Are the comments clear and useful?

- Ensure have checked the comments.
