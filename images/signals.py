from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image

# @receiver(m2m_changed, sender=Image.users_like.through)
# def users_like_changed(sender, instance, **kwargs):
#     instance.total_likes = instance.users_like.count()
#     instance.save()
#     print(instance.total_likes)

@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, action, **kwargs):
    print("sender: {}".format(sender))
    print("instance: {} [{}]".format(instance, instance.__class__.__name__))
    print("action: {}".format(action))
    print("kwargs: {}".format(kwargs))
    if action in ["post_add", "post_remove"]:
        print("instance.users_like: {}".format(instance.users_like))
        print("instance.users_like.count(): {}".format(instance.users_like.count()))
        instance.total_likes = instance.users_like.count()
        print("instance.total_likes: {}".format(instance.total_likes))
        instance.save()
        print("[after save()] instance.total_like: {}".format(instance.total_likes))
    else:
        print("Action isn't post_add or post_remove -> doing nothing")