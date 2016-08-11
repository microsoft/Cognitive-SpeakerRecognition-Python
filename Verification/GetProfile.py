import VerificationServiceHttpClientHelper
import sys

def get_profile(subscription_key, profile_id):
    """Get a speaker's profile with given profile ID
    
    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to resets
    """
    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        subscription_key)
    
    profile = helper.get_profile(profile_id)
    
    print('Profile ID = {0}\nLocale = {1}\nEnrollments Completed = {2}\nRemaining Enrollments = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
        profile._profile_id,
        profile._locale,
        profile._enrollments_count,
        profile._remaining_enrollments_count,
        profile._created_date_time,
        profile._last_action_date_time,
        profile._enrollment_status))
        
        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python DeleteProfile.py <subscription_key> <profile_id> ')
        print('\t<subscription_key> is the subscription key for the service')
        print('\t<profile_id> the ID for a profile to delete from the sevice')
        sys.exit('Error: Incorrect usage.')
    get_profile(sys.argv[1], sys.argv[2])

