# import matplotlib.pyplot as plt
# from matplotlib.gridspec import GridSpec

# def format_axes(fig):
#     for i, ax in enumerate(fig.axes):
#         ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
#         ax.tick_params(labelbottom=False, labelleft=False)


# #for each node, evaluate depth and number of right-turns taken to get to it. These are its coordinates.
# def visualise_dtree_nested_boxes(node, show=False, depth=4):
#     fig = plt.figure(constrained_layout=True)

#     gs = GridSpec(2**(depth-1), 4, figure=fig)
#     ax1 = fig.add_subplot(gs[0, :])
#     # identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
#     ax2 = fig.add_subplot(gs[1, :-1])
#     ax3 = fig.add_subplot(gs[1:, -1])
#     ax4 = fig.add_subplot(gs[-1, 0])
#     ax5 = fig.add_subplot(gs[-1, -2])

#     fig.suptitle("GridSpec")
#     format_axes(fig)

#     plt.show()

# def visualise_dtree_flattened_phase_space(node, show=False):
#     pass

# def visualise_dtree_graph(node, show=False):
#     pass