#include <vector>
#include <opencv2/opencv.hpp>
#include <opencv2/xfeatures2d.hpp>

typedef cv::Ptr<cv::Feature2D> FeaturePtr;
typedef cv::Ptr<cv::DescriptorMatcher> MatcherPtr;


class Detector
{
    std::string name;
    cv::Mat image;
    std::vector<cv::KeyPoint> keypts;
    cv::Mat descriptors;

public:
    Detector(const std::string name, FeaturePtr feature) {}
    static Detector Factory(const std::string name) {}

};
// factory contructor

// detectAndCompute


class Matcher
{
    std::string name;

public:
    Matcher(const std::string name, MatcherPtr matcher) {}
    static Matcher Factory(const std::string name) {}
    void SetRefFeatures(std::vector<cv::KeyPoint>& keypts, cv::Mat descriptors)
    {}
    
};
// factory contructor

// match

// drawMatches



class MatchHandler
{
    std::vector<Detector> refer_dets;
    std::vector<Detector> input_dets;
    float inlierRatio;
    int minMatches;

public:
    // create feature detectors and matchers depending on string inputs
    // set reference image
    MatchHandler(const std::vector<std::string> features, 
                 const std::vector<std::string> matchers, 
                 cv::Mat refimg)
    {
        for(const std::string& feat : features)
            refer_dets.push_back( Detector::Factory(feat) );
        for(const std::string& feat : features)
            input_dets.push_back( Detector::Factory(feat) );
        for(const std::string& feat : features)
            input_dets.push_back( Detector::Factory(feat) );
    }

    // detect features on reference image for all feature types
    void SetRefImage(cv::Mat refimg) {}

    //

};

// detectAndMatch
// float acceptRatio


