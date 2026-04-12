import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
import matplotlib.patheffects as pe

# Taller figure to fit text below hex
fig, ax = plt.subplots(figsize=(6, 7), facecolor='none')
ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.45, 1.15)
ax.set_aspect('equal')
ax.axis('off')

# ── Hexagon background ──────────────────────────────────────────────────────
hex_patch = RegularPolygon(
    (0, 0), numVertices=6, radius=1.08,
    orientation=np.pi / 6,
    facecolor='#0d1b2a', edgecolor='#00c9a7', linewidth=4
)
ax.add_patch(hex_patch)

# ── Streaming dots (incoming observations) — scaled up ──────────────────────
np.random.seed(7)
n_dots = 20
xs = np.linspace(-0.95, -0.32, n_dots)
ys = np.random.uniform(-0.09, 0.09, n_dots)
sizes = np.linspace(20, 75, n_dots)
alphas = np.linspace(0.3, 1.0, n_dots)
colors_stream = plt.cm.cool(np.linspace(0.3, 0.85, n_dots))
for x, y, s, a, c in zip(xs, ys, sizes, alphas, colors_stream):
    ax.scatter(x, y, s=s, color=c, alpha=a, zorder=4)

# ── Central causal fork node ─────────────────────────────────────────────────
center_circle = Circle((0, 0), 0.16, facecolor='#00c9a7', edgecolor='white', linewidth=2.5, zorder=5)
ax.add_patch(center_circle)
ax.text(0, 0, '⊗', ha='center', va='center', fontsize=20, color='#0d1b2a',
        fontweight='bold', zorder=6)

# Arrow from stream to center
ax.annotate('', xy=(-0.17, 0), xytext=(-0.34, 0),
            arrowprops=dict(arrowstyle='->', color='#00c9a7', lw=2.8), zorder=4)

# ── Treatment arm (top-right) ────────────────────────────────────────────────
ax.annotate('', xy=(0.55, 0.40), xytext=(0.15, 0.10),
            arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=2.8,
                            connectionstyle='arc3,rad=-0.15'), zorder=4)
t_xs = np.linspace(0.22, 0.70, 12)
t_ys = np.linspace(0.17, 0.52, 12) + np.random.uniform(-0.03, 0.03, 12)
t_cols = plt.cm.Blues(np.linspace(0.5, 0.95, 12))
for x, y, c in zip(t_xs, t_ys, t_cols):
    ax.scatter(x, y, s=42, color=c, alpha=0.9, zorder=4)

# ── Control arm (bottom-right) ───────────────────────────────────────────────
ax.annotate('', xy=(0.55, -0.40), xytext=(0.15, -0.10),
            arrowprops=dict(arrowstyle='->', color='#f97316', lw=2.8,
                            connectionstyle='arc3,rad=0.15'), zorder=4)
c_xs = np.linspace(0.22, 0.70, 12)
c_ys = np.linspace(-0.17, -0.52, 12) + np.random.uniform(-0.03, 0.03, 12)
c_cols = plt.cm.Oranges(np.linspace(0.5, 0.95, 12))
for x, y, c in zip(c_xs, c_ys, c_cols):
    ax.scatter(x, y, s=42, color=c, alpha=0.9, zorder=4)

# ── CATE convergence line (bottom of hex) ────────────────────────────────────
cate_xs = np.linspace(-0.60, 0.60, 60)
cate_ys = -0.88 + 0.10 * np.exp(-3*(cate_xs-0.5)**2) * np.sin(18*cate_xs) * np.exp(-np.linspace(0, 3, 60))
ax.plot(cate_xs, cate_ys - 0.02, color='#00c9a7', lw=2.0, alpha=0.85, zorder=4)
ax.axhline(-0.90, xmin=0.16, xmax=0.84, color='white', lw=1.0, alpha=0.25, linestyle='--', zorder=3)

# ── "OnlineCML" below the hexagon ────────────────────────────────────────────
ax.text(0, -1.28, 'OnlineCML', ha='center', va='center', fontsize=26,
        color='white', fontweight='bold', zorder=6,
        path_effects=[pe.withStroke(linewidth=4, foreground='#0d1b2a')])

plt.tight_layout(pad=0)
plt.savefig('onlinecml_logo.png', dpi=300, bbox_inches='tight',
            transparent=True, facecolor='none')
plt.savefig('onlinecml_logo_small.png', dpi=100, bbox_inches='tight',
            transparent=True, facecolor='none')
print("Done.")
