"""
Script NetBox pour créer un équipement physique (Device).
Demande : nom, constructeur, modèle (DeviceType) et site.
"""

from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from dcim.choices import DeviceStatusChoices
from extras.scripts import Script, StringVar, ObjectVar, ChoiceVar


class CreateDevice(Script):
    class Meta:
        name = "Create Device"
        description = "Créer un équipement physique en saisissant son nom, constructeur, modèle et site"

    # --- Champs du formulaire affiché dans l'interface NetBox ---

    device_name = StringVar(
        label="Nom de l'équipement",
        description="Nom unique de l'équipement dans NetBox",
    )

    site = ObjectVar(
        model=Site,
        label="Site",
        description="Site d'hébergement de l'équipement",
    )

    manufacturer = ObjectVar(
        model=Manufacturer,
        label="Constructeur",
        description="Filtrera automatiquement les modèles disponibles",
    )

    device_type = ObjectVar(
        model=DeviceType,
        label="Modèle",
        description="Modèle de l'équipement (doit appartenir au constructeur sélectionné)",
        query_params={"manufacturer_id": "$manufacturer"},  # filtre dynamique sur le constructeur
    )

    role = ObjectVar(
        model=DeviceRole,
        label="Rôle",
        description="Rôle fonctionnel de l'équipement (ex. Switch, Serveur, Routeur...)",
    )

    status = ChoiceVar(
        choices=DeviceStatusChoices,
        default=DeviceStatusChoices.STATUS_ACTIVE,
        label="Statut",
    )

    # --- Logique d'exécution ---

    def run(self, data, commit):
        device = Device(
            name=data["device_name"],
            site=data["site"],
            device_type=data["device_type"],   # contient déjà le constructeur
            role=data["role"],
            status=data["status"],
        )

        device.full_clean()   # valide les contraintes NetBox avant d'écrire en base
        device.save()

        self.log_success(
            f"Équipement "
            f"[{device.name}](/dcim/devices/{device.id}/) "
            f"créé sur le site « {device.site} » "
            f"(modèle : {device.device_type}, "
            f"constructeur : {device.device_type.manufacturer})."
        )

        return f"Équipement {device.name} créé avec succès."