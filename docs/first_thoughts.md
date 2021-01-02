### First Thoughts 2-1-2021

---

#### Components (priority list)
1. Web crawler
2. Database
3. Newsletter Adapter
4. Web
5. Own newsletter service

---

###### 1. Web crawler
Automatic (1 / day) web crawler which checks some sections of ulany.sk and saves the new items to the DB. Must be robust like a framework. 

###### 2. Database
Database layer where all information will be stored. SQLite is enough for this project. Probably SQLAlchemy (or more lightweight package) + alembic for create/migration.

**Schema**

| Table         | Type                  |
| :-----------: | :-------------------: |
| id            | int PRIMARY KEY       |
| name          | text                  |
| href          | text                  |
| language      | enum[hu, sk]          |
| added         | datetime on_create    |
| sent_weekly   | NULL datetime         |
| sent_monthly  | NULL datetime         |

###### 3. Newsletter Adapter
Library / class to authenticate & send the newsletter content to the subscribed users. It should be able to work with more plans. In current state there will be 2 plans (weekly and monthly).

- [MailerLite](https://developers.mailerlite.com/reference) + [Python SDK](https://github.com/skoudoro/mailerlite-api-python)
- [Mailchimp](https://mailchimp.com/developer/api/) + [Python SDK](https://github.com/mailchimp/mailchimp-marketing-python)
- [Sender.net](https://api.sender.net/)
- [Omnisend](https://api-docs.omnisend.com/v3/)


###### 4. Web
Simple lightweight web to inform about the project and his options + FAQ. (Direct subscribe if is available or when the own solution will be implemented). Serve just static files for now.

###### 5. Own newsletter service
Really low priority in the list. The last resort when there will be no other option and the whole project will be limited by the free services (eg. no. of subscribers/sent mail reached the limit)


