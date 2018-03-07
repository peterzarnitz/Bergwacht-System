from django.contrib.contenttypes.models import ContentType
 
# List of deleted apps
DEL_APPS = ["trainings"]
 
ct = ContentType.objects.all().order_by("app_label", "model")
 
for c in ct:
    if (c.app_label in DEL_APPS) :
        print "Deleting Content Type %s %s" % (c.app_label, c.model)
        c.delete()
