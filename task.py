import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg', 0)

def pad_image(img, pad):
    h, w = img.shape
    padded = np.zeros((h + 2 * pad, w + 2 * pad), dtype=np.uint8)
    padded[pad:pad + h, pad:pad + w] = img
    return padded

def manual_linear_filter(img, kernel):
    k = kernel.shape[0]
    pad = k // 2
    padded = pad_image(img, pad)
    h, w = img.shape
    output = np.zeros((h, w), dtype=np.float32)
    for i in range(h):
        for j in range(w):
            region = padded[i:i + k, j:j + k]
            output[i, j] = np.sum(region * kernel)
    return np.clip(output, 0, 255).astype(np.uint8)

def manual_median_filter(img, ksize):
    pad = ksize // 2
    padded = pad_image(img, pad)
    h, w = img.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            region = padded[i:i + ksize, j:j + ksize]
            output[i, j] = np.median(region)
    return output

def manual_max_filter(img, ksize):
    pad = ksize // 2
    padded = pad_image(img, pad)
    h, w = img.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            region = padded[i:i + ksize, j:j + ksize]
            output[i, j] = np.max(region)
    return output

def manual_min_filter(img, ksize):
    pad = ksize // 2
    padded = pad_image(img, pad)
    h, w = img.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            region = padded[i:i + ksize, j:j + ksize]
            output[i, j] = np.min(region)
    return output

average_kernel = np.ones((3, 3), dtype=np.float32) / 9
weighted_kernel = np.array([[1, 2, 1],
                            [2, 4, 2],
                            [1, 2, 1]], dtype=np.float32) / 16
laplacian_kernel = np.array([[1, -2, 1],
                             [-2, 4, -2],
                             [1, -2, 1]], dtype=np.float32)

average_result = manual_linear_filter(image, average_kernel)
weighted_result = manual_linear_filter(image, weighted_kernel)
laplacian_result = manual_linear_filter(image, laplacian_kernel)

median_result = manual_median_filter(image, 3)
max_result = manual_max_filter(image, 3)
min_result = manual_min_filter(image, 3)

plt.figure(figsize=(15, 10))

plt.subplot(2, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(2, 4, 2)
plt.imshow(average_result, cmap='gray')
plt.title('Average Filter')
plt.axis('off')

plt.subplot(2, 4, 3)
plt.imshow(weighted_result, cmap='gray')
plt.title('Weighted Filter')
plt.axis('off')

plt.subplot(2, 4, 4)
plt.imshow(laplacian_result, cmap='gray')
plt.title('Laplacian Filter')
plt.axis('off')

plt.subplot(2, 4, 5)
plt.imshow(median_result, cmap='gray')
plt.title('Median Filter')
plt.axis('off')

plt.subplot(2, 4, 6)
plt.imshow(max_result, cmap='gray')
plt.title('Max Filter')
plt.axis('off')

plt.subplot(2, 4, 7)
plt.imshow(min_result, cmap='gray')
plt.title('Min Filter')
plt.axis('off')

plt.tight_layout()
plt.show()