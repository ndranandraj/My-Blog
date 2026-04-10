
import { useState } from "react";

const layers = [
  { id: "author", label: "AUTHORING", color: "#6366f1" },
  { id: "ci", label: "CI / CD", color: "#0ea5e9" },
  { id: "hosting", label: "HOSTING", color: "#10b981" },
  { id: "dns", label: "DNS & CDN", color: "#f59e0b" },
  { id: "analytics", label: "OBSERVABILITY", color: "#ec4899" },
];

const nodes = [
  // Authoring
  {
    id: "local",
    layer: "author",
    icon: "💻",
    title: "Local Machine",
    subtitle: "macOS",
    details: [
      "Hugo v0.160.0 (extended)",
      "Stack theme",
      "Content → Markdown files",
      "Assets → SCSS, images, SVGs",
      "Config → hugo.toml",
    ],
  },
  {
    id: "hugo",
    layer: "author",
    icon: "⚙️",
    title: "Hugo SSG",
    subtitle: "Static Site Generator",
    details: [
      "Converts Markdown → HTML",
      "Processes SCSS → CSS",
      "Minifies assets",
      "Generates sitemap.xml",
      "Creates robots.txt",
    ],
  },
  // CI/CD
  {
    id: "github",
    layer: "ci",
    icon: "🐙",
    title: "GitHub Repo",
    subtitle: "ndranandraj/My-Blog",
    details: [
      "Source of truth",
      "Branch: main",
      "Git push triggers deploy",
      "Stores theme (Stack)",
      "Workflows in .github/",
    ],
  },
  {
    id: "actions",
    layer: "ci",
    icon: "🔄",
    title: "GitHub Actions",
    subtitle: "deploy.yml",
    details: [
      "Trigger: push to main",
      "Step 1: Checkout repo",
      "Step 2: snap install hugo",
      "Step 3: hugo --minify",
      "Step 4: Upload → Pages artifact",
    ],
  },
  // Hosting
  {
    id: "pages",
    layer: "hosting",
    icon: "🌐",
    title: "GitHub Pages",
    subtitle: "Free Static Hosting",
    details: [
      "Serves /public/ folder",
      "HTTPS enforced",
      "Custom domain support",
      "CNAME → ndranandraj.com",
      "_headers for security",
    ],
  },
  // DNS
  {
    id: "cloudflare",
    layer: "dns",
    icon: "☁️",
    title: "Cloudflare",
    subtitle: "Registrar + DNS",
    details: [
      "Domain: ndranandraj.com",
      "CNAME → ndranandraj.github.io",
      "DNS propagation",
      "DDoS protection",
      "SSL/TLS termination",
    ],
  },
  {
    id: "browser",
    layer: "dns",
    icon: "🧑‍💻",
    title: "Visitor's Browser",
    subtitle: "End User",
    details: [
      "Resolves ndranandraj.com",
      "Downloads static HTML/CSS/JS",
      "Zero server round trips",
      "Instant page loads",
      "Dark mode supported",
    ],
  },
  // Observability
  {
    id: "ga",
    layer: "analytics",
    icon: "📊",
    title: "Google Analytics",
    subtitle: "GA4 · G-WG6FZGEPT7",
    details: [
      "Visitor tracking",
      "Page view metrics",
      "Traffic sources",
      "Session duration",
      "Real-time dashboard",
    ],
  },
  {
    id: "gsc",
    layer: "analytics",
    icon: "🔍",
    title: "Search Console",
    subtitle: "Google Search",
    details: [
      "Sitemap submitted",
      "Indexing status",
      "Search impressions",
      "Keyword rankings",
      "Core Web Vitals",
    ],
  },
];

const flows = [
  { from: "local", to: "github", label: "git push" },
  { from: "github", to: "actions", label: "triggers" },
  { from: "actions", to: "pages", label: "deploys artifact" },
  { from: "cloudflare", to: "pages", label: "CNAME" },
  { from: "browser", to: "cloudflare", label: "DNS lookup" },
  { from: "browser", to: "ga", label: "GA4 beacon" },
  { from: "browser", to: "gsc", label: "indexed pages" },
];

const layerColors = {
  author: { bg: "#ede9fe", border: "#6366f1", text: "#4338ca" },
  ci: { bg: "#e0f2fe", border: "#0ea5e9", text: "#0369a1" },
  hosting: { bg: "#d1fae5", border: "#10b981", text: "#065f46" },
  dns: { bg: "#fef3c7", border: "#f59e0b", text: "#92400e" },
  analytics: { bg: "#fce7f3", border: "#ec4899", text: "#9d174d" },
};

export default function ArchDiagram() {
  const [active, setActive] = useState(null);
  const activeNode = nodes.find((n) => n.id === active);

  const nodesByLayer = layers.map((l) => ({
    ...l,
    nodes: nodes.filter((n) => n.layer === l.id),
  }));

  return (
    <div style={{ fontFamily: "'Segoe UI', sans-serif", background: "#f8fafc", minHeight: "100vh", padding: "2rem" }}>
      <div style={{ maxWidth: 900, margin: "0 auto" }}>
        {/* Header */}
        <div style={{ textAlign: "center", marginBottom: "2rem" }}>
          <h1 style={{ fontSize: "1.6rem", fontWeight: 700, color: "#1e293b", margin: 0 }}>
            ndranandraj.com — Architecture Diagram
          </h1>
          <p style={{ color: "#64748b", marginTop: "0.4rem", fontSize: "0.9rem" }}>
            Hugo SSG · GitHub Pages · Cloudflare DNS · GA4
          </p>
        </div>

        {/* Layers */}
        <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          {nodesByLayer.map((layer) => {
            const c = layerColors[layer.id];
            return (
              <div
                key={layer.id}
                style={{
                  background: c.bg,
                  border: `2px solid ${c.border}`,
                  borderRadius: 16,
                  padding: "1rem 1.2rem",
                }}
              >
                <div style={{ fontSize: "0.7rem", fontWeight: 700, letterSpacing: "0.1em", color: c.text, marginBottom: "0.8rem" }}>
                  {layer.label}
                </div>
                <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap" }}>
                  {layer.nodes.map((node) => (
                    <div
                      key={node.id}
                      onClick={() => setActive(active === node.id ? null : node.id)}
                      style={{
                        background: "#fff",
                        border: `2px solid ${active === node.id ? c.border : "#e2e8f0"}`,
                        borderRadius: 12,
                        padding: "0.8rem 1rem",
                        cursor: "pointer",
                        flex: "1 1 160px",
                        transition: "all 0.15s ease",
                        boxShadow: active === node.id ? `0 0 0 3px ${c.border}33` : "0 1px 3px #0001",
                      }}
                    >
                      <div style={{ fontSize: "1.5rem", marginBottom: "0.3rem" }}>{node.icon}</div>
                      <div style={{ fontWeight: 700, fontSize: "0.9rem", color: "#1e293b" }}>{node.title}</div>
                      <div style={{ fontSize: "0.75rem", color: "#94a3b8", marginTop: "0.1rem" }}>{node.subtitle}</div>
                    </div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>

        {/* Detail panel */}
        {activeNode && (
          <div
            style={{
              marginTop: "1.5rem",
              background: "#fff",
              border: `2px solid ${layerColors[activeNode.layer].border}`,
              borderRadius: 14,
              padding: "1.2rem 1.5rem",
              boxShadow: "0 4px 20px #0001",
            }}
          >
            <div style={{ display: "flex", alignItems: "center", gap: "0.7rem", marginBottom: "0.8rem" }}>
              <span style={{ fontSize: "2rem" }}>{activeNode.icon}</span>
              <div>
                <div style={{ fontWeight: 700, fontSize: "1.05rem", color: "#1e293b" }}>{activeNode.title}</div>
                <div style={{ fontSize: "0.8rem", color: "#64748b" }}>{activeNode.subtitle}</div>
              </div>
            </div>
            <ul style={{ margin: 0, paddingLeft: "1.2rem", color: "#334155", fontSize: "0.88rem", lineHeight: 1.9 }}>
              {activeNode.details.map((d, i) => <li key={i}>{d}</li>)}
            </ul>
          </div>
        )}

        {/* Flow legend */}
        <div style={{ marginTop: "1.5rem", background: "#fff", borderRadius: 14, border: "1px solid #e2e8f0", padding: "1rem 1.5rem" }}>
          <div style={{ fontSize: "0.7rem", fontWeight: 700, letterSpacing: "0.1em", color: "#64748b", marginBottom: "0.8rem" }}>
            DATA FLOWS
          </div>
          <div style={{ display: "flex", flexWrap: "wrap", gap: "0.6rem" }}>
            {flows.map((f, i) => {
              const from = nodes.find((n) => n.id === f.from);
              const to = nodes.find((n) => n.id === f.to);
              return (
                <div
                  key={i}
                  style={{
                    background: "#f1f5f9",
                    borderRadius: 8,
                    padding: "0.35rem 0.7rem",
                    fontSize: "0.78rem",
                    color: "#475569",
                    display: "flex",
                    alignItems: "center",
                    gap: "0.3rem",
                  }}
                >
                  <span style={{ fontWeight: 600 }}>{from.icon} {from.title}</span>
                  <span style={{ color: "#94a3b8" }}>→</span>
                  <span style={{ color: "#94a3b8", fontStyle: "italic" }}>{f.label}</span>
                  <span style={{ color: "#94a3b8" }}>→</span>
                  <span style={{ fontWeight: 600 }}>{to.icon} {to.title}</span>
                </div>
              );
            })}
          </div>
        </div>

        <div style={{ textAlign: "center", marginTop: "1.2rem", fontSize: "0.75rem", color: "#94a3b8" }}>
          Click any component card to see details
        </div>
      </div>
    </div>
  );
}
