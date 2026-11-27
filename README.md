<a href="https://bayar.dev">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg">
    <img alt="Namchinbayar Naran — Founder & Lead Engineer at bayar.dev" src="./assets/header-light.svg" width="100%">
  </picture>
</a>

<p align="center">
  <a href="https://bayar.dev"><img alt="bayar.dev" src="https://img.shields.io/badge/bayar.dev-platform-7ee7ff?style=flat-square&labelColor=0d1117"></a>
  <a href="https://bayar.dev/docs"><img alt="Docs" src="https://img.shields.io/badge/docs-read-a78bfa?style=flat-square&labelColor=0d1117"></a>
  <a href="https://www.linkedin.com/in/bayardev"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-bayardev-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=0d1117"></a>
  <a href="https://x.com/bayardotdev"><img alt="X" src="https://img.shields.io/badge/X-@bayardotdev-e6edf3?style=flat-square&logo=x&logoColor=white&labelColor=0d1117"></a>
  <a href="mailto:hi@bayar.dev"><img alt="Email" src="https://img.shields.io/badge/hi@bayar.dev-email-3fb950?style=flat-square&logo=maildotru&logoColor=white&labelColor=0d1117"></a>
</p>

I'm **Bayar**, the solo founder of [**bayar.dev**](https://bayar.dev). I build AI infrastructure in public: the layer between your users and the model. The terminal on the homepage is a real streaming endpoint, and every number on the site is measured.

```ts
const bayar = {
  building: "bayar.dev — a live streaming AI terminal, built in public",
  stage:    "early, bootstrapped, shipping",
  shipped:  ["streaming chat on Claude Haiku 5.5", "per-IP rate limiting",
             "request validation", "hourly benchmarks, raw data public",
             "a one-prompt homepage with a tide under it"],
  now:      "recall: knowledge base, Kafka event stream into MongoDB Atlas, metrics, agent + MCP",
  next:     ["provider failover", "PII guard", "semantic cache", "private VPC / BYOK"],
  later:    "founders access: tools for people who support the work",
  daily:    "CachyOS + niri (Dux Shell), WezTerm + zsh, way too many terminals",
  based:    "Walnut Creek, CA",
};
```

### What a request looks like on bayar.dev

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/flow-dark.svg">
  <img alt="Live request flow: client → per-IP rate limit → validation → Claude Haiku 5.5 through the Anthropic API → stream back. Planned, not shipped: provider failover, PII guard, semantic cache, private VPC and BYOK" src="./assets/flow-light.svg" width="100%">
</picture>

### Measured, not claimed

<!-- BENCH:START -->
<p>
  <a href="https://bayar.dev/benchmarks">
  <img alt="TTFT p50: 505 ms" src="https://img.shields.io/badge/TTFT%20p50-505%20ms-7ee7ff?style=flat-square&labelColor=0d1117">
  <img alt="output p50: 194 tok/s" src="https://img.shields.io/badge/output%20p50-194%20tok%2Fs-a78bfa?style=flat-square&labelColor=0d1117">
  <img alt="success: 100%" src="https://img.shields.io/badge/success-100%25-3fb950?style=flat-square&labelColor=0d1117">
  <img alt="samples: 168" src="https://img.shields.io/badge/samples-168-8b949e?style=flat-square&labelColor=0d1117">
  </a>
</p>

<sub>Claude Haiku 5.5 (low effort), short chat, last 7 days, probed every hour. Method and raw data at <a href="https://bayar.dev/benchmarks">bayar.dev/benchmarks</a>.</sub>
<!-- BENCH:END -->

### Latest from the log

<!-- LOG:START -->
- [The homepage is one prompt now, with a tide under it](https://bayar.dev/log/the-homepage-is-one-prompt-with-a-tide-under-it) · <sub>Nov 14, 2026</sub>
- [What enforcing the CSP cost, and what it could not see](https://bayar.dev/log/what-enforcing-the-csp-cost-and-what-it-could-not-see) · <sub>Nov 14, 2026</sub>
- [The homepage now leads with numbers I measure](https://bayar.dev/log/the-homepage-now-leads-with-numbers-i-measure) · <sub>Nov 14, 2026</sub>
- [All entries →](https://bayar.dev/log)
<!-- LOG:END -->

### Stack

<p>
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white">
  <img alt="Vercel AI SDK" src="https://img.shields.io/badge/Vercel_AI_SDK-000000?style=for-the-badge&logo=vercel&logoColor=white">
  <img alt="Cloudflare" src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white">
  <img alt="AWS CDK" src="https://img.shields.io/badge/AWS_CDK-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white">
  <img alt="Stripe" src="https://img.shields.io/badge/Stripe-635BFF?style=for-the-badge&logo=stripe&logoColor=white">
  <img alt="Claude" src="https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=claude&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="MongoDB Atlas" src="https://img.shields.io/badge/MongoDB_Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white">
  <img alt="Apache Kafka" src="https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white">
  <img alt="Tailscale" src="https://img.shields.io/badge/Tailscale-242424?style=for-the-badge&logo=tailscale&logoColor=white">
  <img alt="CachyOS" src="https://img.shields.io/badge/CachyOS-1793D1?style=for-the-badge&logo=archlinux&logoColor=white">
  <img alt="niri" src="https://img.shields.io/badge/niri-6E56CF?style=for-the-badge&logo=wayland&logoColor=white">
</p>

### Public work

| Project | What it is |
| --- | --- |
| [**recall**](https://bayar.dev/projects#recall) | A personal knowledge base searched by meaning: Voyage embeddings, Atlas vector search, a Kafka event stream, and an MCP server. Private repo |
| [**command-center**](https://bayar.dev/projects#command-center) | A private start page for running bayar.dev, read from Airtable with zero runtime dependencies. Private repo |
| [**tailscale-policy**](https://bayar.dev/projects#tailscale-policy) | My tailnet rules as GitOps: tested on every PR, applied on merge, signed in with GitHub OIDC. Private repo |
| [**starfall-arcade**](https://github.com/namchinbayar/starfall-arcade) | A tiny cosmic browser game: private S3 behind CloudFront, deployed with AWS CDK |
| [**@bayardotdev**](https://github.com/bayardotdev) | The bayar.dev organization |

<sub>ORCID <a href="https://orcid.org/0009-0001-5896-7447">0009-0001-5896-7447</a> · commits signed with SSH via 1Password</sub>
