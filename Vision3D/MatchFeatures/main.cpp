#include <opencv2/opencv.hpp>
#include <iostream>

int main()
{
    cv::Mat img(100, 100, CV_8UC3, 255);
    cv::imshow("image", img);
    cv::waitKey();
    return 0;
}
