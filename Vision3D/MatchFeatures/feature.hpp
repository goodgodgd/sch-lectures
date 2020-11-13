#include <vector>
#include <cassert>
#include <opencv2/opencv.hpp>
#include <opencv2/xfeatures2d.hpp>

typedef cv::Ptr<cv::Feature2D> FeaturePtr;
typedef cv::Ptr<cv::DescriptorMatcher> MatcherPtr;


struct DetectResult
{
    const std::string name;
    cv::Mat image;
    const std::vector<cv::KeyPoint>& keypts;
    cv::Mat descriptors;
};

// Detector holds keypoint detector, descriptor computer and their results
class Detector
{
    FeaturePtr feature;
    std::string name;
    cv::Mat image;
    std::vector<cv::KeyPoint> keypts;
    cv::Mat descriptors;

public:
    Detector(const std::string _name, FeaturePtr _feature)
    {}
    
    static Detector Factory(const std::string name)
    {}
    
    void DetectAndCompute(cv::Mat image)
    {}
    
    DetectResult getResult()
    {
        return {name, image, keypts, descriptors};
    }

    std::string GetName() { return name; }
};


struct MatcherResult
{
    const std::string name;
    const std::vector<cv::DMatch>& matches;
};


class Matcher
{
    MatcherPtr matcher;
    std::string name;
    std::vector<cv::DMatch> matches;
    const int minMathces = 10;

public:
    Matcher(const std::string _name, MatcherPtr _matcher)
    {}
    
    static Matcher Factory(const std::string name)
    {}
    
    std::vector<cv::DMatch>& MatchDescriptors(cv::Mat referDesc, cv::Mat inputDesc)
    {}
    
    static float& AcceptRatio()
    {
        static float acceptRatio = 0.5f;
        return acceptRatio;
    }

    MatcherResult getResult()
    {
        return {name, matches};
    }
};


class MatchHandler
{
    std::vector<Detector> referDets;
    std::vector<Detector> inputDets;
    std::vector<Matcher> matchers;
    float acceptRatio;

public:
    // create feature detectors and matchers depending on string inputs
    MatchHandler(const std::vector<std::string> features, 
                 const std::vector<std::string> matchers)
                 : acceptRatio(0.5f)
    {
        assert(features.size() == matchers.size());
        for(const std::string& feat : features)
            referDets.push_back( Detector::Factory(feat) );
        for(const std::string& feat : features)
            inputDets.push_back( Detector::Factory(feat) );
        for(const std::string& match : matchers)
            matchers.push_back( Matcher::Factory(match) );
    }

    // detect features and compute descriptors on reference image for all feature types
    void SetRefImage(cv::Mat refimg)
    {
        for(auto& det: referDets)
            det.DetectAndCompute(refimg);
    }

    // detect features and compute descriptors on input image for all feature types
    // match input descriptors with reference descriptors
    void MatchImage(cv::Mat inpimg)
    {
        for(auto& det: inputDets)
            det.DetectAndCompute(inpimg);
        
        for(size_t i=0; i<matchers.size(); i++)
        {
            matchers[i].MatchDescriptors(referDets[i].getResult().descriptors, 
                                         inputDets[i].getResult().descriptors);
        }
    }

    // change minimum inlier ratio in Matcher class
    void ChangeAcceptRatio(float change)
    {
        acceptRatio += change;
        acceptRatio = std::max(std::min(acceptRatio, 1.f), 0.f);
        Matcher::AcceptRatio() = acceptRatio;
    }

    // draw match
    cv::Mat DrawMatchResult(int maxHeight=1000)
    {
        std::vector<cv::Mat> resultImgs;
        for(size_t i=0; i<matchers.size(); i++)
        {
            cv::Mat result = DrawSingleResult(
                referDets[i].getResult(), inputDets[i].getResult(), matchers[i].getResult()
            );
            resultImgs.push_back(result);
        }
        cv::Mat stackedResult;
        cv::vconcat(resultImgs, stackedResult);
        // if(stackedResult.rows > maxHeight)
            // cv::resize()
        return stackedResult;
    }

    cv::Mat DrawSingleResult(DetectResult refDet, DetectResult inpDet, MatcherResult match)
    {
    }

};
