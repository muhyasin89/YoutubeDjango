from typing import Any, Sequence

from django.contrib.auth import get_user_model
import factory

class UserFactory(factory.DjangoModelFactory):

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    name = factory.Faker("name")

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]

    @factory.post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        # we need to set current tenant because post_generation() trigger another save/update
        # set_current_tenant(self.account)
        password = factory.Faker(
            "password",
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(
            extra_kwargs={}
        )
        self.set_password(password)



