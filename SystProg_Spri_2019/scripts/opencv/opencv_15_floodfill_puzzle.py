import cv2
import numpy as np
IMG_PATH = "../sample_imgs"
import show_imgs as si

def count_puzzle(img):
    ih, iw, ch = img.shape
    mask = np.zeros((ih+2, iw+2), dtype=np.uint8)
    images = {"original": img.copy()}
    cv2.imshow("image", img)
    cv2.waitKey()
    count = 0
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if mask[y+1, x+1] == 0:
                color = np.random.randint(50, 256, 3).tolist()
                color[0] = 255
                ret, img, mask, rect = cv2.floodFill(img, mask, (x,y), color, (10,10,10), (10,10,10), flags=8)
                mask_show = mask*255
                print(f"area={ret}, rect={rect}, mask value={mask[y+1, x+1]}")
                if ret > 500:
                    cv2.imshow("image", img)
                    cv2.imshow("mask", mask_show)
                    cv2.waitKey(200)
                    count += 1
    print("total puzzle count:", count)
    cv2.destroyAllWindows()
    images["filled"] = img
    result_img = si.show_imgs(images, "floodfill", 2)
    cv2.imwrite(IMG_PATH + "/result/floodfill_puzzle.jpg", result_img)


if __name__ == "__main__":
    image = cv2.imread(IMG_PATH + "/puzzle.jpg")
    count_puzzle(image)
