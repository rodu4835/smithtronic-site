# DNS cutover — moving smithtronic.com from Framer to GitHub Pages

Do these steps **in order**. The live Framer site keeps serving the domain until
step 3, and nothing goes down at any point.

---

## Before you start

- Preview the finished replica at **https://rodu4835.github.io/smithtronic-site/**
  and confirm you're happy with it. Nothing below is reversible-free, but all of
  it is reversible: putting the old Framer records back restores the old site.
- Have your Bluehost login handy (that's where the domain is registered).

---

## Step 1 — Tell GitHub the domain is ours

In this repo: **Settings → Pages → Custom domain** → enter `www.smithtronic.com`
→ Save. GitHub writes a `CNAME` file into the repo (that's expected).

It will warn that DNS isn't configured yet. That's fine — step 2 fixes it.

## Step 2 — Change the web records at Bluehost

Log in to Bluehost → **Domains → smithtronic.com → DNS / Zone Editor**.

**Remove** the existing records that point the site at Framer:
- the `A` record for `@` (host `smithtronic.com`) pointing at a Framer IP
- the `CNAME` for `www` pointing at something like `sites.framer.app`

**Add** these instead:

| Type | Host / Name | Points to | TTL |
|---|---|---|---|
| A | `@` | `185.199.108.153` | default |
| A | `@` | `185.199.109.153` | default |
| A | `@` | `185.199.110.153` | default |
| A | `@` | `185.199.111.153` | default |
| CNAME | `www` | `rodu4835.github.io.` | default |

All four A records are required — they're GitHub's redundant servers.

### ⚠️ Leave these records ALONE

Do **not** touch anything of type **MX**, or any `TXT` record containing `spf`,
`dkim`, or `dmarc`. Those run **email for ron@smithtronic.com**. Changing them
breaks your email; changing the A/CNAME records above does not.

## Step 3 — Wait, then verify

DNS usually propagates in 15–60 minutes (occasionally a few hours).

1. Visit **http://www.smithtronic.com** — you should see the new site.
2. Back in **Settings → Pages**, wait for the green "DNS check successful",
   then tick **Enforce HTTPS** (the padlock certificate is issued automatically
   and free; it can take up to an hour to become available).
3. Check that **https://www.smithtronic.com/shop/auxlightkit/installguide/**
   loads — that's the URL printed on the kit QR cards.
4. Send yourself a test email at ron@smithtronic.com to confirm mail is unaffected.

## Step 4 — Cancel Framer

Only after steps 1–3 check out. From then on your only recurring cost is the
domain renewal at Bluehost.

---

## If something looks wrong

- **Site doesn't load after an hour:** re-check the four A records for typos, and
  make sure no leftover Framer A/CNAME record remains.
- **"Domain does not resolve" in GitHub Pages settings:** DNS hasn't propagated
  yet; wait and re-check.
- **Need to roll back:** restore the original Framer A/CNAME records at Bluehost
  and (if still subscribed) the Framer site serves the domain again.
