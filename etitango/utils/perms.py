from django.contrib.auth.models import Group, Permission

# APPS
from apps.profiles.models import User

# CONTANTS
EventGroup_Perms = [
    # perms only for editors
    'add_blog',
    'change_blog',
    'delete_blog',
    'change_inscription',
    ]

BossGroup_Perms = [
    """
        perms only for Bosses
        all apps "view" perms are assign to Users by default
    """
    # add
    'add_event', 'add_blog', 'add_eventgroup', 'add_eventgroup',
    # change
    'change_event', 'change_blog', 'change_inscription', 'change_eventgroup',
    # delete
    'delete_event', 'delete_blog', 'delete_inscription', 'delete_eventgroup',
    ]

ReviewGroup_Perms = [
    """
        perms only for reviews,
        TODO:
        - [ ] must be change blog for payloads.
    """
    'deny_payload', 'confirm_payload',
]

# BOSS METHODS
def Add_Boss(email):
    """
        Allow manage boss members.

        Boss functions MUST NEVER BE CALLED BY SITE.
        There are created only for admin use.

        TO DO: In the future, it could be integrate (or rewrite) for admin.page.
        Should be allowed only for staff or superuser(admin).
    """
    try:
        bossGroup = Group.objects.get(name="boss")
        newBoss = User.objects.get(email=email)
        newBoss.groups.add(bossGroup)
        console_log.run(email + "now is a boss!")
    except:
        console_log.warn("something happen, check user groups:")
        console_log.warn(newBoss.groups.all())

def Remove_Boss(email):
    try:
        bossGroup = Group.objects.get(name="boss")
        newBoss = User.objects.get(email=email)
        newBoss.groups.remove(bossGroup)
        console_log.run(email + " has not perms anymore", "perms")
    except:
        console_log.warn("something happen, check user groups:")
        console_log.warn(newBoss.groups.all())

# REVIEW METHODS
def Add_Review(email):
    """
        Allow manage review members.
    """
    try:
        reviewGroup = Group.objects.get(name="review")
        newReview = User.objects.get(email=email)
        newReview.groups.add(reviewGroup)
        console_log.run(email + "now is a reviewer!")
    except:
        console_log.warn("something happen, check user groups:")
        console_log.warn(newReview.groups.all())

def Remove_Review(email):
    try:
        reviewGroup = Group.objects.get(name="review")
        newReview = User.objects.get(email=email)
        newReview.groups.remove(reviewGroup)
        console_log.run(email + " has not perms anymore", "perms")
    except:
        console_log.warn("something happen, check user groups:")
        console_log.warn(newReview.groups.all())


# ADMIN METHODS
def DeactivateProfile(email):
    """
        DeactivateProfile will denied acccess to user; also, it save the data, so
        User.email and User.Profile.dni_number can't be use to create new users.
    """
    try:
        user = User.objects.get(email=email)
        user.is_active = False
        user.save()
        console_log.run(email + " now will dance alone, forever.... *evil laugh*", "evil laugh")
    except Exception:
        console_log.warn(email + " repel my powers...")

def Create_SuperGroups():
    """
        This function must be run when the server is installed
        in a new server
    """
    if not Group.objects.filter(name="boss"):
        Group.objects.create(name="boss")
        bossGroup = Group.objects.get(name='boss')
        for perm in BossGroup_Perms:
            p = Permission.objects.get(codename=perm)
            bossGroup.permissions.add(p)
        console_log.run("boss Group Created!")
    else:
        console_log.err("boss created before")

    if not Group.objects.filter(name="review"):
        Group.objects.create(name="review")
        reviewGroup = Group.objects.get(name='review')
        for perm in ReviewGroup_Perms:
            p = Permission.objects.get(codename=perm)
            reviewGroup.permissions.add(p)
        console_log.run("Review Group Created!")
    else:
        console_log.err("Review created before")
