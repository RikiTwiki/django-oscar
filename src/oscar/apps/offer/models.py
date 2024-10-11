# pylint: disable=W0401, W0614
from oscar.apps.offer.abstract_models import (
    AbstractBenefit,
    AbstractCondition,
    AbstractConditionalOffer,
    AbstractRange,
    AbstractRangeProduct,
    AbstractRangeProductFileUpload,
)
from oscar.apps.offer.results import (
    SHIPPING_DISCOUNT,
    ZERO_DISCOUNT,
    BasketDiscount,
    PostOrderAction,
    ShippingDiscount,
)
from oscar.core.loading import is_model_registered

class ConditionIncompatible(Exception):
    pass

__all__ = [
    "BasketDiscount",
    "ShippingDiscount",
    "PostOrderAction",
    "SHIPPING_DISCOUNT",
    "ZERO_DISCOUNT",
    "ConditionalOffer",
    "Condition",
]



class ConditionalOffer(AbstractConditionalOffer):
    def apply_benefit(self, basket, request=None):
        if not self.is_condition_satisfied(basket, request=request):
            return ZERO_DISCOUNT
        return self.benefit.proxy().apply(basket, self.condition.proxy(), self)

    def is_condition_satisfied(self, basket, request=None):
        return self.condition.proxy().is_satisfied(self, basket, request=request)


if not is_model_registered("offer", "Benefit"):

    class Benefit(AbstractBenefit):
        pass

    __all__.append("Benefit")


class Condition(AbstractCondition):
    def is_satisfied(self, offer, basket, request=None):
        return super().is_satisfied(offer=offer, basket=basket)


if not is_model_registered("offer", "Range"):

    class Range(AbstractRange):
        pass

    __all__.append("Range")


if not is_model_registered("offer", "RangeProduct"):

    class RangeProduct(AbstractRangeProduct):
        pass

    __all__.append("RangeProduct")


if not is_model_registered("offer", "RangeProductFileUpload"):

    class RangeProductFileUpload(AbstractRangeProductFileUpload):
        pass

    __all__.append("RangeProductFileUpload")

# Import the benefits and the conditions. Required after initializing the
# parent models to allow overriding them

from oscar.apps.offer.benefits import *
from oscar.apps.offer.conditions import *

from oscar.apps.offer.benefits import __all__ as benefit_classes
from oscar.apps.offer.conditions import __all__ as condition_classes

from oscar.apps.offer.models import *

__all__.extend(benefit_classes)
__all__.extend(condition_classes)
