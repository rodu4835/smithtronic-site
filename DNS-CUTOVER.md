# DNS cutover — moving smithtronic.com from Framer to GitHub Pages

Captured live on 2026-08-06, so the values below are **your actual records**, not
generic advice. Nothing here touches email.

---

## Your DNS today (rollback reference)

Nameservers: `ns1.bluehost.com`, `ns2.bluehost.com` — so DNS is edited **at Bluehost**.

| Type | Host | Current value | What it does |
|---|---|---|---|
| A | `@` | `31.43.160.6` | website → Framer |
| A | `@` | `31.43.161.6` | website → Framer |
| CNAME | `www` | `sites.framer.app` | website → Framer |
| CNAME | `google3a3f442237451e36` | `google.com` | **Google Workspace verification** |
| MX | `@` | `smtp.google.com` (priority 1) | **your email (Google Workspace)** |
| TXT | `@` | `google-site-verification=aVee275JGITBsm_Z3Vaa4NoLZKS335Ur_2kaXwtnxlE` | proves the domain to Google |

If you ever need to undo the cutover, restore the three website rows above.

---

## The change

**Delete** these three (they point at Framer):
- A `@` → `31.43.160.6`
- A `@` → `31.43.161.6`
- CNAME `www` → `sites.framer.app`

**Add** these five (they point at GitHub):

| Type | Host | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `rodu4835.github.io` |

All four A records are needed — they are GitHub's four redundant servers.

### ⚠️ Do not touch these three rows

- **MX `@` → smtp.google.com** — this is ron@smithtronic.com. Deleting it stops your email.
- **TXT `@` → google-site-verification=…** — Google uses it to confirm you own the domain.
- **CNAME `google3a3f442237451e36` → google.com** — also Google Workspace verification.

Changing the A/CNAME rows above does **not** affect email. They are independent.

---

## Order of operations (no downtime)

1. **Open** the Bluehost DNS editor and get to the record list — don't save anything yet.
2. **Tell me you're there.** I set the custom domain on the GitHub side (5 seconds).
   GitHub is then ready to serve smithtronic.com, while Framer is still serving it —
   nothing has changed for visitors yet.
3. **Make the record changes above and save.** This is the moment the switch happens.
4. **Wait 15–60 minutes** for DNS to propagate.
5. **Tell me it's saved** — I'll verify the domain resolves to GitHub, confirm the
   site loads, turn on HTTPS, and re-check that your email records are intact.
6. **Then cancel Framer.** Not before step 5 confirms everything is live.

---

## What to verify before cancelling Framer

- https://www.smithtronic.com loads the new site
- https://smithtronic.com (no www) redirects to it
- https://www.smithtronic.com/shop/auxlightkit/installguide/ loads —
  **this is the URL printed on the QR cards shipped with every kit**
- The padlock (HTTPS) shows, with no browser warning
- Send yourself a test email at ron@smithtronic.com and confirm it arrives

---

## After the cutover

Your only recurring cost is the domain renewal at Bluehost. Hosting is free and
unlimited for a site this size. To change the site, edit the HTML in this repo and
push — it redeploys in about a minute.

### Optional, unrelated to this move

Your domain has **no SPF record**. That's a pre-existing gap, not something this
change causes, but adding one helps your outgoing mail avoid spam folders. If you
want it later, it's a single TXT record on `@`:
`v=spf1 include:_spf.google.com ~all`
