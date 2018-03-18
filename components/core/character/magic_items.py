"""MagicItems components."""

from modules.element import Element, Component


class MagicItemsAddModal(Component):
    """Definition of magicItems add modal component."""

    item_id = 'magicItemsAddItemInput'
    type_id = 'magicItemsAddTypeInput'
    rarity_id = 'magicItemsAddRarityInput'
    max_charges_id = 'magicItemsAddMaxChargesInput'
    charges_id = 'magicItemsAddChargesInput'
    weight_id = 'magicItemsAddWeightInput'
    requires_attunement_id = 'magicItemsAddRequiresAttunementCheckbox'
    attuned_id = 'magicItemsAddAttunedCheckbox'
    description_id = 'magicItemsAddDescriptionTextarea'
    add_id = 'magicItemsAddAddButton'
    cancel_id = 'magicItemsAddCancelButton'

    item = Element(id_=item_id)
    type_ = Element(id_=type_id)
    rarity = Element(id_=rarity_id)
    max_charges = Element(id_=max_charges_id)
    charges = Element(id_=charges_id)
    weight = Element(id_=weight_id)
    requires_attunement = Element(id_=requires_attunement_id)
    attuned = Element(id_=attuned_id)
    description = Element(id_=description_id)
    add = Element(id_=add_id)
    cancel = Element(id_=cancel_id)


class MagicItemsEditModal(Component):
    """Definition of magicItems edit modal component."""

    item_id = 'magicItemsEditItemInput'
    type_id = 'magicItemsEditTypeInput'
    rarity_id = 'magicItemsEditRarityInput'
    max_charges_id = 'magicItemsEditMaxChargesInput'
    charges_id = 'magicItemsEditChargesInput'
    weight_id = 'magicItemsEditWeightInput'
    requires_attunement_id = 'magicItemsEditRequiresAttunementCheckbox'
    attuned_id = 'magicItemsEditAttunedCheckbox'
    description_id = 'magicItemsEditDescriptionTextarea'
    done_id = 'magicItemsEditDoneButton'

    item = Element(id_=item_id)
    type_ = Element(id_=type_id)
    rarity = Element(id_=rarity_id)
    max_charges = Element(id_=max_charges_id)
    charges = Element(id_=charges_id)
    weight = Element(id_=weight_id)
    requires_attunement = Element(id_=requires_attunement_id)
    attuned = Element(id_=attuned_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class MagicItemsPreviewModal(Component):
    """Definition of magicItems preview modal component."""

    item_id = 'magicItemsPreviewItemInput'
    rarity_id = 'magicItemsPreviewRarityInput'
    type_id = 'magicItemsPreviewTypeInput'
    max_charges_id = 'magicItemsPreviewMaxChargesInput'
    weight_id = 'magicItemsPreviewWeightInput'
    description_id = 'magicItemsPreviewDescriptionTextarea'
    done_id = 'magicItemsPreviewDoneButton'

    item = Element(id_=item_id)
    rarity = Element(id_=rarity_id)
    type_ = Element(id_=type_id)
    max_charges = Element(id_=max_charges_id)
    weight = Element(id_=weight_id)
    description = Element(id_=description_id)
    done = Element(id_=done_id)


class MagicItemsModalTabs(Component):
    """Definition of magicItems modal tabs component."""

    preview_id = 'magicItemsModalPreviewTab'
    edit_id = 'magicItemsModalEditTab'

    preview = Element(id_=preview_id)
    edit = Element(id_=edit_id)


class MagicItemsTable(Component):
    """Definition of magicItems edit modal componenet."""

    add_id = 'magicItemsAddIcon'
    table_id = 'magicItemsTable'
    total_weight_id = 'magicItemsTableTotalWeight'
    magic_item_header_id = 'magicItemsMagicItemHeader'
    charges_header_id = 'magicItemsChargesHeader'
    attuned_header_id = 'magicItemsAttunedHeader'
    weight_header_id = 'magicItemsWeightHeader'

    add = Element(id_=add_id)
    table = Element(id_=table_id)
    total_weight = Element(id_=total_weight_id)
    magic_item_header = Element(id_=magic_item_header_id)
    charges_header = Element(id_=charges_header_id)
    attuned_header = Element(id_=attuned_header_id)
    weight_header = Element(id_=weight_header_id)
