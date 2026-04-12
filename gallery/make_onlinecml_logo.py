import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Circle, RegularPolygon
from matplotlib.patheffects import withStroke
import matplotlib.patheffects as pe

fig, ax = plt.subplots(figsize=(6, 6), facecolor='none')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.axis('off')

# ── Hexagon background ──────────────────────────────────────────────────────
hex_patch = RegularPolygon(
    (0, 0), numVertices=6, radius=1.05,
    orientation=np.pi / 6,
    facecolor='#0d1b2a', edgecolor='#00c9a7', linewidth=4
)
ax.add_patch(hex_patch)

# ── Streaming dots (incoming observations) ──────────────────────────────────
np.random.seed(7)
n_dots = 18
xs = np.linspace(-0.85, -0.30, n_dots)
ys = np.random.uniform(-0.08, 0.08, n_dots)
sizes = np.linspace(18, 60, n_dots)
alphas = np.linspace(0.3, 1.0, n_dots)
colors_stream = plt.cm.cool(np.linspace(0.3, 0.85, n_dots))
for x, y, s, a, c in zip(xs, ys, sizes, alphas, colors_stream):
    ax.scatter(x, y, s=s, color=c, alpha=a, zorder=4)

# ── Central causal fork node ────────────────────────────────────────────────
center_circle = Circle((0, 0), 0.13, facecolor='#00c9a7', edgecolor='white', linewidth=2, zorder=5)
ax.add_patch(center_circle)
ax.text(0, 0, '⊗', ha='center', va='center', fontsize=16, color='#0d1b2a',
        fontweight='bold', zorder=6)

# Arrow from stream to center
ax.annotate('', xy=(-0.14, 0), xytext=(-0.30, 0),
            arrowprops=dict(arrowstyle='->', color='#00c9a7', lw=2.5), zorder=4)

# ── Treatment arm (top-right) ───────────────────────────────────────────────
ax.annotate('', xy=(0.48, 0.34), xytext=(0.13, 0.09),
            arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=2.5,
                            connectionstyle='arc3,rad=-0.15'), zorder=4)
t_xs = np.linspace(0.20, 0.62, 10)
t_ys = np.linspace(0.15, 0.44, 10) + np.random.uniform(-0.03, 0.03, 10)
t_cols = plt.cm.Blues(np.linspace(0.5, 0.95, 10))
for x, y, c in zip(t_xs, t_ys, t_cols):
    ax.scatter(x, y, s=35, color=c, alpha=0.9, zorder=4)

ax.text(0.32, 0.62, 'Treatment', ha='center', va='center', fontsize=9,
        color='#38bdf8', fontweight='bold', zorder=6,
        path_effects=[pe.withStroke(linewidth=3, foreground='#0d1b2a')])

# ── Control arm (bottom-right) ──────────────────────────────────────────────
ax.annotate('', xy=(0.48, -0.34), xytext=(0.13, -0.09),
            arrowprops=dict(arrowstyle='->', color='#f97316', lw=2.5,
                            connectionstyle='arc3,rad=0.15'), zorder=4)
c_xs = np.linspace(0.20, 0.62, 10)
c_ys = np.linspace(-0.15, -0.44, 10) + np.random.uniform(-0.03, 0.03, 10)
c_cols = plt.cm.Oranges(np.linspace(0.5, 0.95, 10))
for x, y, c in zip(c_xs, c_ys, c_cols):
    ax.scatter(x, y, s=35, color=c, alpha=0.9, zorder=4)

ax.text(0.32, -0.62, 'Control', ha='center', va='center', fontsize=9,
        color='#f97316', fontweight='bold', zorder=6,
        path_effects=[pe.withStroke(linewidth=3, foreground='#0d1b2a')])

# ── CATE convergence line (bottom of hex) ──────────────────────────────────
cate_xs = np.linspace(-0.55, 0.55, 60)
cate_ys = -0.82 + 0.10 * np.exp(-3 * (cate_xs - 0.5)**2) * np.sin(18 * cate_xs) * np.exp(-np.linspace(0, 3, 60))
ax.plot(cate_xs, cate_ys - 0.02, color='#00c9a7', lw=2.0, alpha=0.85, zorder=4)
ax.axhline(-0.84, xmin=0.18, xmax=0.82, color='white', lw=1.0, alpha=0.3, linestyle='--', zorder=3)

# ── Text ─────────────────────────────────────────────────────────────────────
ax.text(0, -0.60, 'online', ha='center', va='center', fontsize=13,
        color='white', fontweight='light', zorder=6,
        path_effects=[pe.withStroke(linewidth=2, foreground='#0d1b2a')],
        fontstyle='italic')
ax.text(0, -0.73, 'CML', ha='center', va='center', fontsize=19,
        color='#00c9a7', fontweight='bold', zorder=6,
        path_effects=[pe.withStroke(linewidth=3, foreground='#0d1b2a')])

plt.tight_layout(pad=0)
plt.savefig('onlinecml_logo.png', dpi=300, bbox_inches='tight',
            transparent=True, facecolor='none')
plt.savefig('onlinecml_logo_small.png', dpi=100, bbox_inches='tight',
            transparent=True, facecolor='none')
print("Saved onlinecml_logo.png and onlinecml_logo_small.png")
