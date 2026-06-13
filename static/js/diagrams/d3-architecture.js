(function () {
  "use strict";

  var PALETTES = {
    dark: {
      page: "#0a0a0f",
      container: "#111318",
      containerBorder: "rgba(255,255,255,0.06)",
      node: "#1a1d2e",
      nodeBorder: "rgba(255,255,255,0.08)",
      text: "#e2e8f0",
      subtext: "#64748b",
      link: "#334155",
      linkAnimated: "#38bdf8",
      env: "#06b6d4",
      app: "#6366f1",
      data: "#a855f7",
      vpc: "#f97316",
      obs: "#10b981",
      infra: "#eab308",
      glow: "rgba(56,189,248,0.5)",
      subsection: "#1e293b",
    },
    light: {
      page: "#f0f2f5",
      container: "rgba(255,255,255,0.7)",
      containerBorder: "rgba(0,0,0,0.08)",
      node: "#ffffff",
      nodeBorder: "rgba(0,0,0,0.08)",
      text: "#1e293b",
      subtext: "#64748b",
      link: "#cbd5e1",
      linkAnimated: "#0284c7",
      env: "#0891b2",
      app: "#4f46e5",
      data: "#7c3aed",
      vpc: "#ea580c",
      obs: "#059669",
      infra: "#ca8a04",
      glow: "rgba(2,132,199,0.3)",
      subsection: "#f1f5f9",
    },
  };

  function isLight() {
    return (
      document.documentElement.getAttribute("data-theme") === "light"
    );
  }
  function P() {
    return PALETTES[isLight() ? "light" : "dark"];
  }
  function typeColor(p, t) {
    var map = {
      env: p.env,
      app: p.app,
      data: p.data,
      vpc: p.vpc,
      obs: p.obs,
      infra: p.infra,
    };
    return map[t] || p.linkAnimated;
  }
  function containerColor(p, t) {
    var map = {
      vpc: p.vpc,
      cluster: p.linkAnimated,
      obs: p.obs,
      infra: p.infra,
      subsection: p.subsection,
    };
    return map[t] || p.linkAnimated;
  }

  function rectEdge(rect, tx, ty) {
    var cx = rect.x + rect.w / 2,
      cy = rect.y + rect.h / 2;
    var dx = tx - cx,
      dy = ty - cy;
    if (dx === 0 && dy === 0) return { x: cx, y: cy };
    if (Math.abs(dx) * rect.h > Math.abs(dy) * rect.w) {
      var ix = dx > 0 ? rect.x + rect.w : rect.x;
      return { x: ix, y: cy + (dy * (ix - cx)) / dx };
    }
    var iy = dy > 0 ? rect.y + rect.h : rect.y;
    return { x: cx + (dx * (iy - cy)) / dy, y: iy };
  }

  function curvePath(x1, y1, x2, y2) {
    var dx = x2 - x1,
      dy = y2 - y1;
    var adx = Math.abs(dx),
      ady = Math.abs(dy);
    var off = Math.max(adx, ady) * 0.35;
    var cpx1, cpy1, cpx2, cpy2;
    if (ady > adx) {
      cpx1 = x1 + dx * 0.1;
      cpy1 = y1 + (dy > 0 ? off : -off);
      cpx2 = x2 - dx * 0.1;
      cpy2 = y2 - (dy > 0 ? off : -off);
    } else {
      cpy1 = y1 + dy * 0.1;
      cpx1 = x1 + (dx > 0 ? off : -off);
      cpy2 = y2 - dy * 0.1;
      cpx2 = x2 - (dx > 0 ? off : -off);
    }
    return (
      "M " +
      x1 +
      "," +
      y1 +
      " C " +
      cpx1 +
      "," +
      cpy1 +
      " " +
      cpx2 +
      "," +
      cpy2 +
      " " +
      x2 +
      "," +
      y2
    );
  }

  function getIcon(type, id) {
    var map = {
      dev: "\u25C9",
      staging: "\u25C9",
      production: "\u25C9",
      webhook: "\u26A1",
      "workflow-engine": "\u2699",
      executions: "\u25B6",
      schedules: "\u23F0",
      credentials: "\uD83D\uDD11",
      redis: "\u26A1",
      rabbitmq: "\uD83D\uDCE8",
      nats: "\uD83D\uDCE1",
      postgresql: "\uD83D\uDCC4",
      minio: "\uD83D\uDEE2",
      "private-subnets": "\uD83C\uDF10",
      "nat-gateway": "\uD83D\uDD04",
      "security-groups": "\uD83D\uDEE1",
      prometheus: "\uD83D\uDCC8",
      grafana: "\uD83D\uDCCA",
      loki: "\uD83D\uDCCB",
      alertmanager: "\uD83D\uDD14",
      docker: "\uD83D\uDC33",
      helm: "\u26F5",
      "kubernetes-infra": "\u2699",
      ingress: "\uD83D\uDEAA",
      "cert-manager": "\uD83D\uDCDC",
      hpa: "\uD83D\uDCCF",
    };
    return map[id] || "\u25CF";
  }

  // ─── Main ────────────────────────────────────────────
  function render(container) {
    if (container.dataset._archRendered) return;
    container.dataset._archRendered = "1";

    var jsonEl = container.querySelector(
      'script[type="application/architecture+json"]'
    );
    if (!jsonEl) return;
    var data = JSON.parse(jsonEl.textContent);
    var p = P();

    var svg = d3.select(container).select("svg");
    var rect = container.getBoundingClientRect();
    var W = rect.width || 1100,
      H = rect.height || 830;

    svg.selectAll("*").remove();
    svg.attr("viewBox", "0 0 1100 830");
    svg.style("background", p.page);

    var g = svg.append("g").attr("class", "zoom-group");
    var zoom = d3.zoom()
      .scaleExtent([0.3, 3])
      .on("zoom", function (e) {
        g.attr("transform", e.transform);
      });
    svg.call(zoom);

    var defs = svg.append("defs");

    // Glow filter
    defs
      .append("filter")
      .attr("id", "glow")
      .append("feGaussianBlur")
      .attr("stdDeviation", 3)
      .attr("result", "blur");
    defs
      .select("#glow")
      .append("feMerge")
      .selectAll("feMergeNode")
      .data(["blur", "SourceGraphic"])
      .enter()
      .append("feMergeNode")
      .attr("in", function (d) {
        return d;
      });

    // Arrow markers
    defs
      .append("marker")
      .attr("id", "arrow")
      .attr("viewBox", "0 0 10 10")
      .attr("refX", 9)
      .attr("refY", 5)
      .attr("markerWidth", 6)
      .attr("markerHeight", 6)
      .attr("orient", "auto")
      .append("path")
      .attr("d", "M 0 0 L 10 5 L 0 10 z")
      .attr("fill", p.link);

    defs
      .append("marker")
      .attr("id", "arrow-ani")
      .attr("viewBox", "0 0 10 10")
      .attr("refX", 9)
      .attr("refY", 5)
      .attr("markerWidth", 6)
      .attr("markerHeight", 6)
      .attr("orient", "auto")
      .append("path")
      .attr("d", "M 0 0 L 10 5 L 0 10 z")
      .attr("fill", p.linkAnimated);

    // Background group
    var bg = g.append("g").attr("class", "bg");

    // ─── Containers ────────────────────────────────────
    if (data.containers) {
      data.containers.forEach(function (c) {
        var tc = containerColor(p, c.type);
        var grp = bg.append("g").attr("class", "arch-container");

        // Outer glow / border
        grp
          .append("rect")
          .attr("x", c.x)
          .attr("y", c.y)
          .attr("width", c.w)
          .attr("height", c.h)
          .attr("rx", 14)
          .attr("fill", "none")
          .attr("stroke", tc)
          .attr("stroke-width", 1)
          .attr("stroke-opacity", 0.3)
          .attr("class", "container-glow");

        // Fill
        grp
          .append("rect")
          .attr("x", c.x + 1)
          .attr("y", c.y + 1)
          .attr("width", c.w - 2)
          .attr("height", c.h - 2)
          .attr("rx", 13)
          .attr("fill", c.type === "subsection" ? p.subsection : p.container)
          .attr("fill-opacity", c.type === "subsection" ? 0.5 : 0.8)
          .attr("class", "container-fill");

        // Inner border
        grp
          .append("rect")
          .attr("x", c.x + 6)
          .attr("y", c.y + 6)
          .attr("width", c.w - 12)
          .attr("height", c.h - 12)
          .attr("rx", 10)
          .attr("fill", "none")
          .attr("stroke", tc)
          .attr("stroke-width", 0.5)
          .attr("stroke-opacity", 0.15);

        // Label
        grp
          .append("text")
          .attr("x", c.x + 16)
          .attr("y", c.y + c.h - 12)
          .attr("fill", tc)
          .attr("fill-opacity", 0.5)
          .attr("font-size", 11)
          .attr("font-weight", 600)
          .attr("font-family", "ui-monospace, monospace")
          .attr("letter-spacing", "1px")
          .text(c.label.toUpperCase());

        // Section divider line
        if (c.type !== "subsection") {
          grp
            .append("line")
            .attr("x1", c.x + 14)
            .attr("y1", c.y + 32)
            .attr("x2", c.x + c.w - 14)
            .attr("y2", c.y + 32)
            .attr("stroke", tc)
            .attr("stroke-width", 0.5)
            .attr("stroke-opacity", 0.15);
        }
      });
    }

    // ─── Build lookup ──────────────────────────────────
    var lookup = {};
    (data.containers || []).forEach(function (c) {
      lookup[c.id] = { x: c.x, y: c.y, w: c.w, h: c.h, isContainer: true };
    });
    (data.nodes || []).forEach(function (n) {
      lookup[n.id] = { x: n.x, y: n.y, w: n.w, h: n.h, isContainer: false };
    });

    // ─── Links ─────────────────────────────────────────
    var lg = g.append("g").attr("class", "links");

    data.links.forEach(function (link) {
      var src = lookup[link.source];
      var tgt = lookup[link.target];
      if (!src || !tgt) return;

      var scx = src.x + src.w / 2,
        scy = src.y + src.h / 2;
      var tcx = tgt.x + tgt.w / 2,
        tcy = tgt.y + tgt.h / 2;

      var p1 = rectEdge(src, tcx, tcy);
      var p2 = rectEdge(tgt, scx, scy);

      var d = curvePath(p1.x, p1.y, p2.x, p2.y);
      var isAnimated = link.animated;
      var style = link.style || "solid";

      // Hit area
      lg.append("path")
        .attr("d", d)
        .attr("fill", "none")
        .attr("stroke", "transparent")
        .attr("stroke-width", 12);

      // Visible path
      var pathEl = lg
        .append("path")
        .attr("d", d)
        .attr("fill", "none")
        .attr("stroke", isAnimated ? p.linkAnimated : p.link)
        .attr("stroke-width", isAnimated ? 2 : 1.5)
        .attr("stroke-dasharray", style === "dashed" ? "6,5" : style === "dotted" ? "2,5" : "none")
        .attr("stroke-opacity", isAnimated ? 0.9 : 0.6)
        .attr("marker-end", isAnimated ? "url(#arrow-ani)" : "url(#arrow)")
        .attr("class", "arch-link")
        .attr("data-link-key", link.source + "-" + link.target);

      // Label
      if (link.label) {
        var pEl = pathEl.node();
        try {
          var len = pEl.getTotalLength();
          var mid = pEl.getPointAtLength(len / 2);
          var lw = link.label.length * 7.5 + 12;
          lg.append("rect")
            .attr("x", mid.x - lw / 2)
            .attr("y", mid.y - 9)
            .attr("width", lw)
            .attr("height", 18)
            .attr("rx", 4)
            .attr("fill", p.page)
            .attr("fill-opacity", 0.85)
            .attr("class", "link-label-bg");
          lg.append("text")
            .attr("x", mid.x)
            .attr("y", mid.y + 4)
            .attr("text-anchor", "middle")
            .attr("fill", p.subtext)
            .attr("font-size", 10)
            .attr("font-family", "ui-monospace, monospace")
            .text(link.label)
            .attr("class", "link-label");
        } catch (_) {}
      }
    });

    // ─── Nodes ─────────────────────────────────────────
    var ng = g.append("g").attr("class", "nodes");

    data.nodes.forEach(function (n) {
      var tc = typeColor(p, n.type);
      var grp = ng.append("g").attr("class", "arch-node").attr("data-id", n.id);

      // Shadow
      grp
        .append("rect")
        .attr("x", n.x + 2)
        .attr("y", n.y + 2)
        .attr("width", n.w)
        .attr("height", n.h)
        .attr("rx", 8)
        .attr("fill", "rgba(0,0,0,0.25)")
        .attr("filter", "url(#glow)");

      // Background
      grp
        .append("rect")
        .attr("x", n.x)
        .attr("y", n.y)
        .attr("width", n.w)
        .attr("height", n.h)
        .attr("rx", 8)
        .attr("fill", p.node)
        .attr("stroke", p.nodeBorder)
        .attr("stroke-width", 1)
        .attr("class", "node-bg");

      // Left accent bar
      grp
        .append("rect")
        .attr("x", n.x + 2)
        .attr("y", n.y + 6)
        .attr("width", 3)
        .attr("height", n.h - 12)
        .attr("rx", 1.5)
        .attr("fill", tc);

      // Icon
      var icon = getIcon(n.type, n.id);
      grp
        .append("text")
        .attr("x", n.x + 18)
        .attr("y", n.y + n.h / 2 + 1)
        .attr("text-anchor", "middle")
        .attr("dominant-baseline", "central")
        .attr("font-size", 16)
        .text(icon)
        .attr("class", "node-icon");

      // Label
      var lines = n.label.split("\n");
      var labelGrp = grp
        .append("text")
        .attr("x", n.x + 34)
        .attr("y", n.y + n.h / 2)
        .attr("fill", p.text)
        .attr("font-size", 12)
        .attr("font-weight", 600)
        .attr("font-family", "system-ui, sans-serif")
        .attr("dominant-baseline", "central");
      labelGrp
        .selectAll("tspan")
        .data(lines)
        .enter()
        .append("tspan")
        .attr("x", n.x + 34)
        .attr("dy", function (_, i) {
          return i === 0 ? 0 : 14;
        })
        .text(function (d) {
          return d;
        });

      // Pulse dot on env and workflow-engine
      if (
        n.type === "env" ||
        n.id === "workflow-engine" ||
        n.id === "k8s-container"
      ) {
        grp
          .append("circle")
          .attr("cx", n.x + n.w - 12)
          .attr("cy", n.y + 12)
          .attr("r", 4)
          .attr("fill", tc)
          .attr("class", "pulse-dot");
      }
    });

    // ─── Particle Animation ────────────────────────────
    var particles = [];
    data.links.forEach(function (link) {
      if (!link.animated) return;
      var pathEl = svg.select('[data-link-key="' + link.source + "-" + link.target + '"]');
      if (pathEl.empty()) return;
      var pNode = pathEl.node();
      var len;
      try {
        len = pNode.getTotalLength();
      } catch (_) {
        return;
      }
      if (!len || len < 1) return;

      var src = lookup[link.source];
      var tc = src && !src.isContainer ? typeColor(p, data.nodes.find(function (n) { return n.id === link.source; })?.type) : p.linkAnimated;

      // Primary particle
      var dot1 = g
        .append("circle")
        .attr("r", 3.5)
        .attr("fill", tc)
        .attr("filter", "url(#glow)")
        .attr("class", "particle");
      particles.push({
        el: dot1.node(),
        path: pNode,
        len: len,
        progress: Math.random(),
        speed: 1 / (2200 + Math.random() * 1200),
      });

      // Secondary dimmer particle (offset phase)
      var dot2 = g
        .append("circle")
        .attr("r", 2)
        .attr("fill", tc)
        .attr("opacity", 0.4)
        .attr("class", "particle");
      particles.push({
        el: dot2.node(),
        path: pNode,
        len: len,
        progress: (Math.random() + 0.4) % 1,
        speed: 1 / (2800 + Math.random() * 1500),
      });
    });

    var lastTime = performance.now();
    var rafId;

    function tick(time) {
      var dt = time - lastTime;
      lastTime = time;
      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];
        p.progress = (p.progress + p.speed * dt) % 1;
        // Clamp to valid range for getPointAtLength
        var t = Math.max(0, Math.min(1, p.progress));
        try {
          var pt = p.path.getPointAtLength(t * p.len);
          p.el.setAttribute("cx", pt.x);
          p.el.setAttribute("cy", pt.y);
        } catch (_) {}
      }
      rafId = requestAnimationFrame(tick);
    }
    if (particles.length > 0) {
      rafId = requestAnimationFrame(tick);
    }

    // ─── Pulse Animation ───────────────────────────────
    var pulseInterval = setInterval(function () {
      svg
        .selectAll(".pulse-dot")
        .transition()
        .duration(600)
        .attr("r", 6)
        .attr("opacity", 0.5)
        .transition()
        .duration(600)
        .attr("r", 4)
        .attr("opacity", 1);
    }, 2500);

    // Cleanup on removal
    container._archCleanup = function () {
      if (rafId) cancelAnimationFrame(rafId);
      clearInterval(pulseInterval);
    };

    // ─── Theme Sync ────────────────────────────────────
    var obs = new MutationObserver(function () {
      var np = P();
      // Background
      svg.style("background", np.page);

      // Arrow markers
      d3.select("#arrow").select("path").attr("fill", np.link);
      d3.select("#arrow-ani").select("path").attr("fill", np.linkAnimated);

      // Containers
      svg.selectAll(".arch-container").each(function () {
        var el = d3.select(this);
        var c = data.containers.find(function (c2) {
          return (
            Math.abs(c2.x - +el.select(".container-fill").attr("x")) < 2
          );
        });
        if (!c) return;
        var tc = containerColor(np, c.type);
        el.select(".container-fill")
          .attr("fill", c.type === "subsection" ? np.subsection : np.container);
        el.select(".container-glow").attr("stroke", tc);
        el.selectAll("text").attr("fill", tc);
      });

      // Links
      svg
        .selectAll(".arch-link")
        .attr("stroke", function () {
          var key = this.getAttribute("data-link-key");
          if (!key) return np.link;
          var found = data.links.find(function (l) {
            return l.source + "-" + l.target === key;
          });
          return found && found.animated ? np.linkAnimated : np.link;
        });
      svg.selectAll(".link-label-bg").attr("fill", np.page);
      svg.selectAll(".link-label").attr("fill", np.subtext);

      // Nodes
      svg.selectAll(".arch-node").each(function () {
        var id = this.getAttribute("data-id");
        var n = data.nodes.find(function (n2) {
          return n2.id === id;
        });
        if (!n) return;
        var tc = typeColor(np, n.type);
        d3.select(this)
          .select(".node-bg")
          .attr("fill", np.node)
          .attr("stroke", np.nodeBorder);
        d3.select(this).selectAll("text").attr("fill", np.text);
        d3.select(this).selectAll(".pulse-dot").attr("fill", tc);
      });

      // Particles
      svg.selectAll(".particle").each(function () {
        // Color is set at creation time; refresh on theme change
        // Simplest: find matching link and compute new color
        // For now, just toggle opacity
      });
    });
    obs.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-theme"],
    });

    // Zoom to fit
    var x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    (data.nodes || []).forEach(function (n) {
      if (n.x < x0) x0 = n.x;
      if (n.y < y0) y0 = n.y;
      if (n.x + n.w > x1) x1 = n.x + n.w;
      if (n.y + n.h > y1) y1 = n.y + n.h;
    });
    (data.containers || []).forEach(function (c) {
      if (c.x < x0) x0 = c.x;
      if (c.y < y0) y0 = c.y;
      if (c.x + c.w > x1) x1 = c.x + c.w;
      if (c.y + c.h > y1) y1 = c.y + c.h;
    });
    var pad = 30;
    x0 -= pad; y0 -= pad; x1 += pad; y1 += pad;
    var cw = x1 - x0, ch = y1 - y0;
    var s = Math.min(W / cw, H / ch, 1);
    var tx = (W - cw * s) / 2 - x0 * s;
    var ty = (H - ch * s) / 2 - y0 * s;
    svg.call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(s));

    container.classList.add("arch-ready");
  }

  // ─── Init ────────────────────────────────────────────
  function init() {
    document.querySelectorAll(".d3-architecture").forEach(render);
  }
  if (
    document.readyState === "complete" ||
    document.readyState === "interactive"
  ) {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
