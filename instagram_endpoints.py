# some query ID or hash code can change, use with care

BASE_URL = 'https://www.instagram.com'
LOGIN_URL = 'https://www.instagram.com/accounts/login/ajax/'
LOGOUT_URL = 'https://www.instagram.com/accounts/logout/'
ACCOUNT_PAGE = 'https://www.instagram.com/{username}'
MEDIA_LINK = 'https://www.instagram.com/p/{code}'
ACCOUNT_MEDIAS = 'https://www.instagram.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables={variables}'
ACCOUNT_JSON_INFO = 'https://www.instagram.com/{username}/?__a=1'
MEDIA_JSON_INFO = 'https://www.instagram.com/p/{code}/?__a=1'
MEDIA_JSON_BY_LOCATION_ID = 'https://www.instagram.com/explore/locations/{{facebookLocationId}}/?__a=1&max_id={{maxId}}'
MEDIA_JSON_BY_TAG = 'https://www.instagram.com/explore/tags/{tag}/?__a=1&max_id={max_id}'
GENERAL_SEARCH = 'https://www.instagram.com/web/search/topsearch/?query={query}'
ACCOUNT_JSON_INFO_BY_ID = 'ig_user({userId}){id,username,external_url,full_name,profile_pic_url,biography,followed_by{count},follows{count},media{count},is_private,is_verified}'
COMMENTS_BEFORE_COMMENT_ID_BY_CODE = 'https://www.instagram.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables={variables}'
LAST_LIKES_BY_CODE = 'ig_shortcode({{code}}){likes{nodes{id,user{id,profile_pic_url,username,follows{count},followed_by{count},biography,full_name,media{count},is_private,external_url,is_verified}},page_info}}'
LIKES_BY_SHORTCODE = 'https://www.instagram.com/graphql/query/?query_id=17864450716183058&variables={"shortcode":"{{shortcode}}","first":{{count}},"after":"{{likeId}}"}'
FOLLOWING_URL = 'https://www.instagram.com/graphql/query/?query_id=17874545323001329&variables={variables}'
FOLLOWING_URL_HASH = 'https://www.instagram.com/graphql/query/?query_hash=c56ee0ae1f89cdbd1c89e2bc6b8f3d18&variables={variables}'
FOLLOWERS_URL = 'https://www.instagram.com/graphql/query/?query_id=17851374694183129&variables={variables}'
FOLLOWERS_URL_HASH = 'https://www.instagram.com/graphql/query/?query_hash=56066f031e6239f35a904ac20c9f37d9&variables={variables}'
FOLLOW_URL = 'https://www.instagram.com/web/friendships/{{accountId}}/follow/'
UNFOLLOW_URL = 'https://www.instagram.com/web/friendships/{{accountId}}/unfollow/'
USER_FEED = 'https://www.instagram.com/graphql/query/?query_id=17861995474116400&fetch_media_item_count=12&fetch_media_item_cursor=&fetch_comment_count=4&fetch_like=10'
USER_FEED2 = 'https://www.instagram.com/?__a=1'
INSTAGRAM_QUERY_URL = 'https://www.instagram.com/query/'
INSTAGRAM_CDN_URL = 'https://scontent.cdninstagram.com/'
ACCOUNT_JSON_PRIVATE_INFO_BY_ID = 'https://i.instagram.com/api/v1/users/{userId}/info/'
ACCOUNT_MEDIAS2 = 'https://www.instagram.com/graphql/query/?query_id=17880160963012870&id={{accountId}}&first=10&after='

HASHTAG_URL = 'https://www.instagram.com/graphql/query/?query_hash=f92f56d47dc7a55b606908374b43a314&variables={variables}'

# look alike?
URL_SIMILAR = 'https://www.instagram.com/graphql/query/?query_id=17845312237175864&id=4663052'
GRAPH_QL_QUERY_URL = 'https://www.instagram.com/graphql/query/?query_id={{queryId}}'

# / **
# *id = {{accoundId}}, first = {{count}}, after = {{mediaId}}
# * /
USER_MEDIAS = '17880160963012870'
USER_STORIES = '17890626976041463'
STORIES = '17873473675158481'

STORIES_UA = 'Instagram 52.0.0.8.83 (iPhone; CPU iPhone OS 11_4 like Mac OS X; en_US; en-US; scale=2.00; 750x1334) ' \
             'AppleWebKit/605.1.15 '
CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 ' \
                'Safari/537.36 '

MAX_CONCURRENT_DOWNLOADS = 5
CONNECT_TIMEOUT = 90
MAX_RETRIES = 5
RETRY_DELAY = 5
MAX_RETRY_DELAY = 60
MAX_MEDIA_PER_PAGE = 50
MAX_MEDIA_DOWNLOADS = 50
