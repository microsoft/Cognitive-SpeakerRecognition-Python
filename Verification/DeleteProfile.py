import VerificationServiceHttpClientHelper
import sys

def delete_profile(subscription_key, profile_id):
    """Delete the given profile from the server
        
    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to reset
    """
    
    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(subscription_key)
    
    helper.delete_profile(profile_id)
    
    print('Profile {0} has been successfully deleted.'.format(profile_id))
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python DeleteProfile.py <subscription_key> <profile_id> ')
        print('\t<subscription_key> is the subscription key for the service')
        print('\t<profile_id> the ID for a profile to delete from the sevice')
        sys.exit('Error: Incorrect usage.')
    
    delete_profile(sys.argv[1], sys.argv[2])
    
