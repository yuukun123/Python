# import matplotlib.pyplot as plt
# import numpy as np
#
# # Your 3D array
# array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#
# # Create subplots for each layer
# fig, axs = plt.subplots(1, 2, figsize=(8, 4))
# for i in range(array_3d.shape[0]):
#     axs[i].imshow(array_3d[i], cmap='viridis', interpolation='nearest')
#     axs[i].set_title(f'Layer {i}')
#     axs[i].set_xticks([0, 1])
#     axs[i].set_yticks([0, 1])
#     plt.colorbar(axs[i].imshow(array_3d[i], cmap='viridis'), ax=axs[i])
#
# plt.tight_layout()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Mảng 3 chiều
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#
# # Tạo mặt nạ cho voxels (ở đây tất cả các giá trị đều > 0 nên hiển thị toàn bộ)
# mask = arr > 0
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Vẽ voxels với màu sắc theo giá trị
# ax.voxels(mask, facecolors=plt.cm.viridis(arr / arr.max()), edgecolor='k')
#
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Mảng 3 chiều
arr = np.array([[[1, 2], [3, 4]] , [[5, 6], [7, 8]] ])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vẽ từng điểm và gán nhãn là giá trị của phần tử
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        for k in range(arr.shape[2]):
            ax.scatter(i, j, k, color='blue')
            ax.text(i, j, k, str(arr[i,j,k]), color='red', fontsize=12, ha='center')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

