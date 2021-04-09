import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"
NON_REGION = 50
AREA_THR = 100
LABEL_BEGIN = 100


def count_balls():
    srcimg = cv2.imread(IMG_PATH + "/ballpool.jpg", cv2.IMREAD_COLOR)
    images, mask = prepare_mask(srcimg)
    result_img = si.show_imgs(images, "floodfill", 3)
    label = LABEL_BEGIN
    ih, iw, ch = srcimg.shape
    hueimg = images["hue"].copy()
    for v in range(0, ih, 5):
        for u in range(0, iw, 5):
            if mask[v+1, u+1] == 0:
                hueimg, mask, area = fill_image(hueimg, mask, (u, v), label)
                cv2.imshow("floodfill mask", mask)
                if area > AREA_THR:
                    label += 1
                    cv2.waitKey(100)
    cv2.waitKey()
    labeled = colorize_regions(mask, label)
    images["labeled balls"] = labeled
    result_img = si.show_imgs(images, "floodfill", 3)
    cv2.imwrite(IMG_PATH + "/result/floodfill_ball.jpg", result_img)


def prepare_mask(srcimg):
    ih, iw, ch = srcimg.shape
    images = {"original": srcimg}
    hsvimg = cv2.cvtColor(srcimg, cv2.COLOR_BGR2HSV)
    images["hue"] = hsvimg[:, :, 0]
    images["saturation"] = hsvimg[:, :, 1]
    images["value"] = hsvimg[:, :, 2]
    # create invalid mask by saturtion and value to set borders of balls
    canny = cv2.Canny(images["value"], 80, 160)
    ret, nonregion = cv2.threshold(canny, 10, NON_REGION, cv2.THRESH_BINARY)
    nonregion[images["value"] < 70] = NON_REGION
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # nonregion = cv2.morphologyEx(nonregion, cv2.MORPH_CLOSE, kernel)
    images["nonregion mask"] = nonregion
    # create floodfill mask with size of (ih+2, iw+2)
    mask = np.zeros((ih+2, iw+2), dtype=np.uint8)
    mask[1:-1, 1:-1] = nonregion
    return images, mask


def fill_image(hueimg, mask, pt, label):
    flags = (4 | cv2.FLOODFILL_MASK_ONLY | (label << 8))
    mask_tmp = mask.copy()
    ret, hueimg, mask_tmp, rect = cv2.floodFill(hueimg, mask_tmp, pt, None, 1, 1, flags=flags)
    print(f"floodfiil at {pt}, pixels={ret}, rect={rect}, label={label}")
    if ret > AREA_THR:
        mask = mask_tmp
    else:   # if region is too small, fill it with NON_REGION
        flags = (4 | cv2.FLOODFILL_MASK_ONLY | (NON_REGION << 8))
        ret, hueimg, mask, rect = cv2.floodFill(hueimg, mask, pt, None, 1, 1, flags=flags)
    return hueimg, mask, ret


def colorize_regions(mask, max_label):
    image = np.zeros((mask.shape[0], mask.shape[1], 3), np.uint8)
    for label in range(LABEL_BEGIN, max_label, 1):
        image[mask==label, :] = np.random.randint(50, 256, 3)
    return image[1:-1, 1:-1, :]


if __name__ == "__main__":
    count_balls()
