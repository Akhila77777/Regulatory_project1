# DermaScan infrastructure (scaffolding / stubs).
# SIMULATION / TRAINING EXERCISE - resource bodies are placeholders; nothing is deployed.
# Full architecture and regulatory mapping: DEP-001. Keep all data/compute in an EU region.

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      # version = "TODO pin"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region # EU region for GDPR data residency (DG-001)
}

# --- Container registry (SDP-001 config items) ---
# resource "google_artifact_registry_repository" "images" { ... }  # TODO

# --- Inference service: Cloud Run (ARC-001 C1-C9; REQ-014, availability KPI) ---
# resource "google_cloud_run_v2_service" "dermascan_api" { ... }   # TODO
#   Notes: require authentication (REQ-050); place behind Load Balancer + Cloud Armor (REQ-054).

# --- Storage: model artifacts + governed datasets (REQ-041; DG-001/DSC-001) ---
# resource "google_storage_bucket" "models"   { ... }  # TODO (EU location, versioning on)
# resource "google_storage_bucket" "datasets" { ... }  # TODO (EU location, restricted IAM)

# --- Security: IAM least privilege + secrets (REQ-050; RISK-010) ---
# resource "google_secret_manager_secret" "api_keys" { ... }  # TODO

# --- Edge protection: Cloud Armor / WAF (REQ-054; RISK-008) ---
# resource "google_compute_security_policy" "armor" { ... }  # TODO

# --- Observability: logging/audit + monitoring (REQ-040/042; KPI-001; RISK-004/006) ---
# Cloud Logging / Audit Logs are enabled at project level; Vertex AI Model Monitoring configured
# with the deployed model for drift/skew detection.  # TODO
