import subsystem_1
import subsystem_2

if __name__ == '__main__':
    testdata_path = "input/open_palm.webm"
    output_file_name = "label.txt"

    landmarks_file = subsystem_1.start(testdata_path, enable_hand_detection=True,
                                       framesToProcess=50, displayNailDetection=True, 
                                       displayLandmarkExtraction=False)

    subsystem_2.start(landmarks_file, output_file_name)
