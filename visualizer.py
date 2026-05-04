# visualizer.py
import matplotlib.pyplot as plt

def plot_single(algo_name, path, seek, disk_size):
    """Plots just one algorithm, saves, and OPENS the image"""
    plt.figure(figsize=(8, 5))
    plt.step(range(len(path)), path, where='post', linewidth=2.5, color='#1f77b4', marker='o')
    plt.title(f"{algo_name} Algorithm\nTotal Seek: {seek} cylinders", fontweight='bold')
    plt.xlabel("Request Sequence"); plt.ylabel("Track Number")
    plt.ylim(-10, disk_size + 10); plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    filename = f"{algo_name.lower()}_graph.png"
    plt.savefig(filename)
    plt.show()  
    plt.close()
    return filename

def plot_comparison(all_data, disk_size):
    """Plots all 4 algorithms overlaid on top of each other"""
    plt.figure(figsize=(12, 7))
    colors = ['red', 'green', 'blue', 'orange']
    
    for i, (name, path, seek) in enumerate(all_data):
        plt.step(range(len(path)), path, where='post', label=f"{name} ({seek} seek)", linewidth=2, color=colors[i])

    plt.title("Disk Scheduling Comparison (Overlaid)", fontsize=16, fontweight='bold')
    plt.xlabel("Sequence Step", fontsize=12); plt.ylabel("Track Number", fontsize=12)
    plt.ylim(-10, disk_size + 10); plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=11); plt.tight_layout()
    plt.savefig("comparison_overlay.png")
#    plt.close()

def plot_comparison_grid(all_data, disk_size):
    """Plots all 4 algorithms in a 2x2 grid side-by-side"""
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    axs = axs.flatten()
    colors = ['#e63946', '#2a9d8f', '#457b9d', '#f4a261'] 
    
    for i, (name, path, seek) in enumerate(all_data):
        axs[i].step(range(len(path)), path, where='post', linewidth=2.5, color=colors[i], marker='o', markersize=4)
        axs[i].set_title(f"{name}\nSeek Time: {seek}", fontweight='bold', fontsize=12)
        axs[i].set_xlabel("Step"); axs[i].set_ylabel("Track")
        axs[i].set_ylim(-10, disk_size + 10)
        axs[i].grid(True, linestyle='--', alpha=0.5)

    plt.suptitle("Disk Scheduling Algorithms (Grid View)", fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig("comparison_grid.png")
 #   plt.close()