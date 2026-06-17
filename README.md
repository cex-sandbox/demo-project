# Demo Project — tiêu dùng Security Template

Minh hoạ một project tích hợp `cex-sandbox/security-template` qua git submodule.

- Template nhúng tại `security/` (submodule, public → không cần token)
- Workflow `.github/workflows/security.yml` copy từ template (tự nhận ngữ cảnh submodule: dùng `security/.semgrep/rules/security.yml`)
- Pipeline chạy trên mọi PR: Gitleaks + Semgrep CRITICAL chặn PR; các scan khác cảnh báo

Xem 2 PR demo: một PR sạch (pass) và một PR chứa lỗi (bị chặn).
