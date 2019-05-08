# from __future__ import print_function
import logging.config
import time
from datetime import datetime

import requests

# from DB.schema_definition import Post, InstagramPost, InstagramUser, Author
# from commons.commons import compute_post_guid, date_to_str, compute_author_guid_by_author_name
# from commons.method_executor import Method_Executor

import json

# from preprocessing_tools.instagram_crawler.instagram_endpoints import *

__author__ = "Joshua Grogin"


# class InstagramCrawler(Method_Executor):
#     def __init__(self, db):
#         super(InstagramCrawler, self).__init__(db)
#         self._comment_per_submission_limit = self._config_parser.eval(self.__class__.__name__,
#                                                                       "max_object_without_saving")
#         self.username = ''
#         self.password = ''
#         self.insta_crawler = InstagramCrawlerAgent(self.username, self.password)

#     def execute(self, window_start=None):
#         posts = self.insta_crawler.get_user_posts(528817151)
#         followedby = self.insta_crawler.get_user_followed_by(528817151)
#         following = self.insta_crawler.get_user_following(528817151)
#         comments = self.insta_crawler.get_post_comments_by_short_code('Bw5JHjhg8DQ')
#         italy = self.insta_crawler.get_posts_by_hashtag('italy')
#         user = self.insta_crawler.get_profile_info('nasa')
#         print("Insta done!")
#         iposts = [self._json_post_to_db_post_converter(post) for post in posts + italy['posts']]
#         iposts += [self._json_post_to_db_instagram_post_converter(post) for post in posts + italy['posts']]
#         self._db.addPosts(iposts)
#         icomments = [self._json_comment_to_db_comment_converter(c) for c in comments]
#         icomments += [self._json_comment_to_db_instagram_comment_converter(c) for c in comments]
#         self._db.addPosts(icomments)
#         to_add = [self._json_user_to_db_author_converter(u) for u in followedby + following + [user]]
#         to_add += [self._json_user_to_db_instagram_user_converter(u) for u in followedby + following + [user]]
#         self._db.addPosts(to_add)
        

#     def _json_post_to_db_post_converter(self, post, domain=u"Instagram_post"):
#         rpost = Post()
#         rpost.post_osn_id = unicode(post[u'id'])
#         rpost.created_at = datetime.fromtimestamp(post[u'taken_at_timestamp'])
#         rpost.author = post[u'owner'][u'id']
#         rpost.author_guid = compute_author_guid_by_author_name(rpost.author)
#         rpost.url = unicode('https://www.instagram.com/p/{}/'.format(post[u'shortcode']))
#         rpost.content = u', '.join(x[u'node'][u'text'] for x in post[u'edge_media_to_caption'][u'edges'])
#         rpost.guid = compute_post_guid(rpost.url, rpost.post_osn_id, date_to_str(rpost.created_at))
#         rpost.domain = domain
#         rpost.post_type = domain
#         rpost.post_id = rpost.guid
#         return rpost

#     def _json_post_to_db_instagram_post_converter(self, post, domain=u"Instagram_post"):
#         ipost = InstagramPost()
#         ipost.id = post[u'id']
#         ipost.comment_count = post[u'edge_media_to_comment'][u'count']
#         ipost.comments_disabled = post[u'comments_disabled']
#         ipost.dimensions = dimensions = json.dumps(post[u'dimensions'])
#         ipost.display_url = post[u'display_url']
#         ipost.gating_info = gating_info = post.setdefault(u'gating_info', None)
#         ipost.instagram_typename = json.dumps(post[u'__typename'])
#         ipost.is_video = post[u'is_video']
#         ipost.likes = post[u'edge_media_preview_like'][u'count']
#         ipost.media_preview = json.dumps(post.setdefault(u'media_preview', 'null'))
#         ipost.shortcode = post[u'shortcode']
#         ipost.thumbnail_resources = json.dumps(post[u'thumbnail_resources'])
#         ipost.hashtag = post.setdefault(u'hashtag', None)
#         return ipost

#     def _json_comment_to_db_comment_converter(self, post, domain=u"Instagram_comment"):
#         rpost = Post()
#         rpost.post_osn_id = unicode(post[u'id'])
#         rpost.created_at = datetime.fromtimestamp(post[u'created_at'])
#         rpost.author = post[u'owner'][u'id']
#         rpost.author_guid = compute_author_guid_by_author_name(rpost.author)
#         rpost.url = unicode('https://www.instagram.com/p/{}/'.format(post[u'shortcode']))
#         rpost.content = post[u'text']
#         rpost.guid = compute_post_guid(rpost.url, rpost.post_osn_id, date_to_str(rpost.created_at))
#         rpost.domain = domain
#         rpost.post_type = domain
#         rpost.post_id = rpost.guid
#         return rpost

#     def _json_comment_to_db_instagram_comment_converter(self, post, domain=u"Instagram_comment"):
#         ipost = InstagramPost()
#         ipost.id = post[u'id']
#         ipost.display_url = post[u'owner'][u'profile_pic_url']
#         ipost.instagram_typename = domain
#         ipost.shortcode = post[u'shortcode']
#         return ipost

#     def _json_user_to_db_author_converter(self, user, domain=u'Instagram_author'):
#         author = Author()
#         author.name = user['username']
#         author.author_screen_name = author.name
#         author.author_guid = compute_author_guid_by_author_name(author.name)
#         author.domain = domain
#         author.author_type = domain
#         author.author_osn_id = user['id']
#         author.author_full_name = user['full_name']
#         author.description = user.setdefault('biography', None)
#         author.url = u'https://www.instagram.com/' + author.author_screen_name
#         author.profile_image_url = user['profile_pic_url']
#         return author

#     def _json_user_to_db_instagram_user_converter(self, user, domain=u'Instagram_author'):
#         author = InstagramUser()
#         author.id = user['id']
#         author.description = user['biography']
#         author.followers_count = user.setdefault('followers_count', None)
#         author.following_count = user.setdefault('following_count', None)
#         author.is_business_account = user.setdefault('is_business_account', None)
#         author.is_joined_recently = user.setdefault('is_joined_recently', None)
#         author.is_private = user.setdefault('is_private', None)
#         author.posts_count = user.setdefault('posts_count', None)
#         return author


class InstagramCrawlerAgent:
    def __init__(self, username, password):
        self.user_data = {}
        self.password = password
        self.username = username
        self.session = requests.Session()
        self.cookies = self.session.cookies
        self.logged_in = False
        self.login(username, password)
        self.last_json = {}

    def login(self, username, password):
        """Logs in to instagram."""
        self.session.headers.update({'Referer': BASE_URL, 'user-agent': STORIES_UA})
        req = self.session.get(BASE_URL)
        self.session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
        login_data = {'username': self.username, 'password': self.password}
        login = self.session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        self.session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        self.cookies = login.cookies
        login_text = json.loads(login.text)
        # print(login_text)
        if login_text.get('authenticated') and login.status_code == 200:
            self.logged_in = True
            self.session.headers = {'user-agent': CHROME_WIN_UA}
        else:
            raise Exception("Instagram login failed")

    def logout(self):
        """Logs out of instagram."""
        if self.logged_in:
            logout_data = {'csrfmiddlewaretoken': self.cookies['csrftoken']}
            self.session.post(LOGOUT_URL, data=logout_data)
            self.logged_in = False

    def get_profile_info(self, username):
        if self.logged_in is False:
            return
        url = ACCOUNT_JSON_INFO.format(username=username)
        response = self.get_json(url)

        if response is None:
            return
        try:
            user_info = json.loads(response.text)['graphql']['user']
            user_info = {
                'username': username,
                'biography': user_info['biography'],
                'followers_count': user_info['edge_followed_by']['count'],
                'following_count': user_info['edge_follow']['count'],
                'full_name': user_info['full_name'],
                'id': user_info['id'],
                'is_business_account': user_info['is_business_account'],
                'is_joined_recently': user_info['is_joined_recently'],
                'is_private': user_info['is_private'],
                'posts_count': user_info['edge_owner_to_timeline_media']['count'],
                'profile_pic_url': user_info['profile_pic_url']
            }
        except (KeyError, IndexError, StopIteration):
            return
        return user_info

    def _get_general_query(self, type_id, id, media_form, container, URL, max_items=MAX_MEDIA_DOWNLOADS):
        items = []
        end_cursor = 'null'
        variables = '"{type_id}":"{id}","first":{max_media},"after":{end_cursor}'
        url = URL.format(variables='{' + variables.format(type_id=type_id, id=id, max_media=MAX_MEDIA_PER_PAGE,
                                                          end_cursor=end_cursor) + '}')
        response = self.get_json(url)
        total = json.loads(response.text)[u'data'][media_form][container][u'count']
        i = 0
        while True:
            data = json.loads(response.text)[u'data'][media_form][container]
            items += [item[u'node'] for item in data[u'edges']]
            print(
                "\rInstagramCrawler finished {0}/{1} of user {2}'s {3}".format((i + 1) * MAX_MEDIA_PER_PAGE, total, id,
                                                                               container), end='')
            if not data[u'page_info'][u'has_next_page'] or i * MAX_MEDIA_PER_PAGE >= max_items:
                break
            i += 1
            end_cursor = data[u'page_info'][u'end_cursor']
            variables = '"{type_id}":"{id}","first":{max_media},"after":"{end_cursor}"'
            url = URL.format(variables='{' + variables.format(type_id=type_id, id=id, max_media=MAX_MEDIA_PER_PAGE,
                                                              end_cursor=end_cursor) + '}')
            response = self.get_json(url)

        return items

    def _get_user_query(self, user_id, container, URL, max_items=MAX_MEDIA_DOWNLOADS):
        return self._get_general_query('id', user_id, u'user', container, URL, max_items)

    def _get_short_code_query(self, short_code, container, URL, max_items=MAX_MEDIA_DOWNLOADS):
        return self._get_general_query('shortcode', short_code, u'shortcode_media', container, URL, max_items)

    def get_user_posts(self, user_id, max_items=MAX_MEDIA_DOWNLOADS):
        return self._get_user_query(user_id, u'edge_owner_to_timeline_media', ACCOUNT_MEDIAS, max_items)

    def get_user_followed_by(self, user_id, max_items=MAX_MEDIA_DOWNLOADS):
        return self._get_user_query(user_id, u'edge_followed_by', FOLLOWERS_URL_HASH, max_items)

    def get_user_following(self, user_id, max_items=MAX_MEDIA_DOWNLOADS):
        return self._get_user_query(user_id, u'edge_follow', FOLLOWING_URL_HASH, max_items)

    def get_post_comments_by_short_code(self, short_code, max_items=MAX_MEDIA_DOWNLOADS):
        comments = self._get_short_code_query(short_code, u'edge_media_to_comment', COMMENTS_BEFORE_COMMENT_ID_BY_CODE,
                                              max_items)
        for comment in comments:
            comment[u'shortcode'] = short_code
        return comments

    def get_posts_by_hashtag(self, tag_name, max_items=MAX_MEDIA_DOWNLOADS):
        res = {
            u'posts': self._get_general_query('tag_name', tag_name, u'hashtag', u'edge_hashtag_to_media', HASHTAG_URL,
                                              max_items)}
        for p in res[u'posts']:
            p[u'hashtag'] = tag_name
        data = json.loads(self.last_json.text)[u'data'][u'hashtag']
        res[u'id'] = data[u'id']
        res[u'name'] = data[u'name']
        res[u'profile_pic_url'] = data[u'profile_pic_url']
        return res

    def get_json(self, *args, **kwargs):
        """Retrieve text from url. Return text as string or None if no data present """
        self.last_json = self.safe_get(*args, **kwargs)
        return self.last_json

    def safe_get(self, *args, **kwargs):
        retry = 0
        retry_delay = RETRY_DELAY
        while True:
            try:
                response = self.session.get(timeout=CONNECT_TIMEOUT, cookies=self.cookies, *args, **kwargs)
                if response.status_code == 404:
                    return
                response.raise_for_status()
                content_length = response.headers.get('Content-Length')
                if content_length is not None and len(response.content) != int(content_length):
                    raise requests.exceptions.RequestException('Partial response')
                return response
            except KeyboardInterrupt:
                raise
            except requests.exceptions.RequestException as e:
                if retry < MAX_RETRIES:
                    time.sleep(retry_delay)
                    retry_delay = min(2 * retry_delay, MAX_RETRY_DELAY)
                    retry = retry + 1
                    continue
                raise e


class StubMockup(object):
    def __new__(cls, **attributes):
        result = object.__new__(cls)
        result.__dict__ = attributes
        return result
