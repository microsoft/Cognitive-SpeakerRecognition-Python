# Microsoft Speaker Recognition API: Python Sample
This repo contains Python samples (using Python 3) to demonstrate the use of Microsoft Speaker Recognition API, an offering within [Microsoft Cognitive Services](https://www.microsoft.com/cognitive-services), formerly known as Project Oxford.
* [Learn about the Speaker Recognition API](https://www.microsoft.com/cognitive-services/en-us/speaker-recognition-api)
* [Read the documentation](https://www.microsoft.com/cognitive-services/en-us/speaker-recognition-api/documentation)
* [Find more SDKs & Samples](https://www.microsoft.com/cognitive-services/en-us/SDK-Sample?api=speaker%20recognition)

## Run the Sample
First, you must obtain a free Speaker Recognition API subscription key by [following the instructions on our website](<https://www.microsoft.com/cognitive-services/en-us/sign-up>).

To use this sample application, there are four different scenarios:
 1. Create a user profile: `python Identification\CreateProfile.py <subscription_key>`
 2. Print all user profiles: `python Identification\PrintAllProfiles.py <subscription_key>`
 3. Enroll user profiles: `python Identification\EnrollProfile.py <subscription_key> <profile_id> <enrollment_file_path>`
 4. Identify test files: `python Identification\IdentifyFile.py <subscription_key> <identification_file_path> <profile_ids>...`

## Contributing
We welcome contributions. Feel free to file issues and pull requests on the repo and we'll address them as we can. Learn more about how you can help on our [Contribution Rules & Guidelines](</CONTRIBUTING.md>). 

You can reach out to us anytime with questions and suggestions using our communities below:
 - **Support questions:** [StackOverflow](<https://stackoverflow.com/questions/tagged/microsoft-cognitive>)
 - **Feedback & feature requests:** [Cognitive Services UserVoice Forum](<https://cognitive.uservoice.com>)

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


## License
All Microsoft Cognitive Services SDKs and samples are licensed with the MIT License. For more details, see
[LICENSE](</LICENSE.md>).

Sample images are licensed separately, please refer to [LICENSE-IMAGE](</LICENSE-IMAGE.md>).
