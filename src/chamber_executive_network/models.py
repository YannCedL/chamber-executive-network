"""
Person and Executive Role Models
"""

from typing import Optional, List
from pydantic import BaseModel, Field

# modeles pour representer les dirigeants et leurs mandats sociaux

class ExecutiveRole(BaseModel):
    title: str = Field(..., description="Titre du mandat (PDG, Gérant, Administrateur, etc.)")
    company_siren: str = Field(..., description="SIREN de l'entreprise cible")
    company_name: str = Field(..., description="Nom de l'entreprise")
    start_date: Optional[str] = Field(None, description="Date de prise de fonction")
    status: str = Field(default="en cours", description="Statut du mandat")

class PersonProfile(BaseModel):
    full_name: str = Field(..., description="Nom complet du dirigeant")
    nationality: Optional[str] = Field(default="Française", description="Nationalité")
    birth_year: Optional[str] = Field(None, description="Année de naissance")
    roles: List[ExecutiveRole] = Field(default_factory=list, description="Liste des mandats")
