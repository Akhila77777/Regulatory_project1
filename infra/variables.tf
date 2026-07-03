# DermaScan infrastructure variables (scaffolding).
# SIMULATION / TRAINING EXERCISE - nothing is deployed. See DEP-001.

variable "project_id" {
  description = "GCP project ID (use a dedicated project per environment: dev/staging/prod)."
  type        = string
}

variable "region" {
  description = "GCP region. MUST be an EU region for GDPR data residency (DEP-001, DG-001)."
  type        = string
  default     = "europe-west3" # Frankfurt
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "dev"
}

variable "image_uri" {
  description = "Container image URI in Artifact Registry for the inference service."
  type        = string
  default     = "" # TODO set by CI/CD (Cloud Build)
}
