# Feature Specification: VM Creation GPU Profile Support

**Feature Branch**: `812-vm-mk-gpu-support`  
**Created**: 2026-04-06  
**Status**: Clarified  
**Input**: User description: "Integrate newly introduced support for creating vms with gpus in pyvss following the same patterns for options in vss-cli compute vm mk from-clib, vss-cli compute vm mk from-clone, from-template"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Deploy VM from Template with GPU (Priority: P1)

As a cloud administrator, I want to specify one or more GPU profiles when creating a virtual machine from a template so that the VM is provisioned with the appropriate vGPU hardware from the start, without needing separate post-deployment steps.

**Why this priority**: Template-based deployment is the most common VM provisioning method. Adding GPU support at creation time eliminates the current multi-step workflow (deploy then attach each GPU), saving time and reducing errors.

**Independent Test**: Can be fully tested by running `vss-cli compute vm mk from-template --gpu-profile <profile> ...` and verifying the resulting request includes the GPU profile(s) in its payload. Delivers immediate value by enabling GPU-attached VM deployment in a single command.

**Acceptance Scenarios**:

1. **Given** a valid GPU profile exists in the infrastructure, **When** the user runs `vss-cli compute vm mk from-template --gpu-profile <profile-name> --source <template> --description "GPU VM" <vm-name>`, **Then** a VM deployment request is submitted with the specified GPU profile included in the payload.
2. **Given** the user needs multiple GPUs, **When** the user runs `vss-cli compute vm mk from-template --gpu-profile <profile-A> --gpu-profile <profile-B> ...`, **Then** a VM deployment request is submitted with both GPU profiles in the payload as a list.
3. **Given** the user does not provide `--gpu-profile`, **When** the user runs `vss-cli compute vm mk from-template` with the other required options, **Then** the VM is deployed without GPU (existing behavior unchanged).
4. **Given** the user provides an invalid or non-existent GPU profile, **When** the command is executed, **Then** a clear error message is displayed indicating the profile was not found.
5. **Given** a valid GPU profile, **When** the user uses shell autocompletion on the `--gpu-profile` option, **Then** available GPU profiles from the infrastructure are listed for selection.

---

### User Story 2 - Deploy VM from Clone with GPU (Priority: P1)

As a cloud administrator, I want to specify one or more GPU profiles when cloning a virtual machine so that the cloned VM has the required vGPU hardware attached upon creation.

**Why this priority**: Clone-based deployment is equally critical and follows the same option patterns as template deployment. Users cloning GPU-enabled VMs or adding GPU to clones need the same first-class support.

**Independent Test**: Can be fully tested by running `vss-cli compute vm mk from-clone --gpu-profile <profile> ...` and verifying the GPU profile(s) appear in the submitted request.

**Acceptance Scenarios**:

1. **Given** a valid GPU profile and a source VM, **When** the user runs `vss-cli compute vm mk from-clone --gpu-profile <profile-name> --source <vm> --description "Cloned GPU VM"`, **Then** a clone request is submitted with the GPU profile in the payload.
2. **Given** the user needs multiple GPUs, **When** the user specifies `--gpu-profile` multiple times, **Then** all GPU profiles are included in the payload as a list.
3. **Given** the user does not provide `--gpu-profile`, **When** the user clones a VM, **Then** the clone proceeds without GPU (existing behavior unchanged).
4. **Given** an invalid GPU profile, **When** the command is executed, **Then** the user sees an error message about the unrecognized profile.

---

### User Story 3 - Deploy VM from Content Library with GPU (Priority: P1)

As a cloud administrator, I want to specify one or more GPU profiles when deploying a VM from a Content Library item so that the deployed VM includes the requested vGPU device(s) from the start.

**Why this priority**: Content Library deployment is the third major provisioning path. All three creation methods must have consistent GPU support to avoid user confusion and maintain a uniform CLI experience.

**Independent Test**: Can be fully tested by running `vss-cli compute vm mk from-clib --gpu-profile <profile> ...` and verifying the GPU profile(s) are included in the deployment request payload.

**Acceptance Scenarios**:

1. **Given** a valid GPU profile and a Content Library item, **When** the user runs `vss-cli compute vm mk from-clib --gpu-profile <profile-name> --source <clib-item> --description "CLib GPU VM" <vm-name>`, **Then** a deployment request is submitted with the specified GPU profile.
2. **Given** the user needs multiple GPUs, **When** the user specifies `--gpu-profile` multiple times, **Then** all GPU profiles are included in the payload as a list.
3. **Given** the user omits `--gpu-profile`, **When** the user deploys from Content Library, **Then** the VM is deployed without GPU (existing behavior unchanged).
4. **Given** an invalid GPU profile name, **When** the command is executed, **Then** an error message indicates the profile was not found.

---

### User Story 4 - Deploy VM from Shell, Image, and Spec with GPU (Priority: P2)

As a cloud administrator, I want to also specify one or more GPU profiles when creating an empty shell VM, deploying from an OVA/OVF image, or creating from another VM's spec so that all VM creation paths support GPU provisioning consistently.

**Why this priority**: While less common than template/clone/clib, shell, image, and spec-based creation should also support GPU for completeness and consistency. This prevents edge cases where administrators must use a multi-step workflow only for these creation methods.

**Independent Test**: Can be fully tested by running `vss-cli compute vm mk shell --gpu-profile <profile> ...`, `vss-cli compute vm mk from-image --gpu-profile <profile> ...`, or `vss-cli compute vm mk from-spec --gpu-profile <profile> ...` and verifying the GPU profile(s) in the payload.

**Acceptance Scenarios**:

1. **Given** a valid GPU profile, **When** the user creates a shell VM with `--gpu-profile`, **Then** the request payload includes the GPU profile(s).
2. **Given** a valid GPU profile, **When** the user deploys from an image with `--gpu-profile`, **Then** the request payload includes the GPU profile(s).
3. **Given** a valid GPU profile, **When** the user creates from a spec with `--gpu-profile`, **Then** the request payload includes the GPU profile(s).
4. **Given** the user omits `--gpu-profile` on shell, image, or spec commands, **Then** existing behavior is unchanged.

---

### Edge Cases

- What happens when the user provides a GPU profile name that matches multiple profiles partially? The existing lookup mechanism returns the first match — this behavior should be consistent with how other type-based lookups (firmware, storage type) work.
- How does the system handle a GPU profile combined with `--instances > 1` (multi-VM deployment)? The GPU profile(s) should be included in each instance's payload without any special handling.
- What happens if a GPU profile is specified for a domain that does not support GPU? The API backend handles validation and returns an appropriate error; the CLI surfaces this error clearly.
- What happens if `--gpu-profile` is specified along with incompatible options (e.g., certain firmware types)? The API handles validation — the CLI passes the profile through to the backend.
- What happens when the user specifies the same GPU profile multiple times? Each occurrence is resolved and included in the list — the API backend determines whether duplicates are valid.
- What happens when one of several specified GPU profiles is invalid? The CLI should fail fast on the first invalid profile before submitting the request.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The CLI MUST accept an optional, repeatable `--gpu-profile` option on the `vss-cli compute vm mk from-template` command.
- **FR-002**: The CLI MUST accept an optional, repeatable `--gpu-profile` option on the `vss-cli compute vm mk from-clone` command.
- **FR-003**: The CLI MUST accept an optional, repeatable `--gpu-profile` option on the `vss-cli compute vm mk from-clib` command.
- **FR-004**: The CLI MUST accept an optional, repeatable `--gpu-profile` option on the `vss-cli compute vm mk shell` command.
- **FR-005**: The CLI MUST accept an optional, repeatable `--gpu-profile` option on the `vss-cli compute vm mk from-image` command.
- **FR-006**: The CLI MUST accept an optional, repeatable `--gpu-profile` option on the `vss-cli compute vm mk from-spec` command.
- **FR-007**: When `--gpu-profile` is provided one or more times, the CLI MUST resolve each profile name/description to its type identifier using the same lookup mechanism used by the existing `vss-cli compute vm set gpu mk` command.
- **FR-008**: When `--gpu-profile` is provided, the CLI MUST include a list of resolved GPU profiles in the request payload sent to the API.
- **FR-009**: When `--gpu-profile` is not provided, the CLI MUST NOT include a GPU key in the payload, preserving full backward compatibility.
- **FR-010**: The `--gpu-profile` option MUST provide shell autocompletion listing available GPU profiles from the infrastructure.
- **FR-011**: If any specified GPU profile cannot be resolved, the CLI MUST display a user-friendly error message and halt command execution before submitting the request.
- **FR-012**: The `--gpu-profile` option MUST work correctly in combination with multi-instance deployments (`--instances > 1`).

### Key Entities

- **GPU Profile**: A vGPU hardware profile identified by a type string and human-readable description. Represents a specific GPU configuration (e.g., NVIDIA GRID vGPU profile) available in the compute domain. Multiple profiles can be attached to a single VM.
- **VM Deployment Request**: The API request payload for creating a new virtual machine, which now optionally includes a list of GPU profile types.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can deploy a GPU-equipped VM in a single command across all three primary creation methods (from-template, from-clone, from-clib) without any post-deployment configuration steps.
- **SC-002**: Users can attach multiple GPU profiles to a VM at creation time by specifying `--gpu-profile` multiple times in a single command.
- **SC-003**: 100% of existing VM creation commands continue to function identically when `--gpu-profile` is not specified (zero regression).
- **SC-004**: GPU profile autocompletion returns available profiles within the same response time as other autocompletion options (e.g., firmware, storage type).
- **SC-005**: All six VM creation commands (`from-template`, `from-clone`, `from-clib`, `shell`, `from-image`, `from-spec`) present a consistent `--gpu-profile` option with identical behavior and help text.
- **SC-006**: Invalid GPU profile input produces a clear error message within the same interaction, without submitting a malformed request to the API.

## Assumptions

- The `pyvss` library already supports a `gpus` parameter (a list) in all its VM creation API methods — confirmed by inspecting method signatures for `deploy_vm_from_template`, `create_vm_from_clone`, `deploy_vm_from_clib_item`, `create_vm`, `create_vm_from_image`, and their multi-instance variants (`deploy_vms_from_template`, `create_vms_from_clone`, `create_vms`). The CLI is integrating support that the backend API already provides.
- The GPU profile resolution mechanism (`get_vm_gpu_profiles_by_name_or_desc`) and autocompletion function (`vm_gpu_profiles`) already exist in the codebase and are reused without modification.
- The existing `gpu_profile_opt` click option definition (used by `set gpu mk`) uses `--profile` with `-p` short flag and `required=True`. A new non-required, repeatable variant with `--gpu-profile` naming will be created for the creation commands to avoid flag conflicts (e.g., `-p` is used by `--custom-spec` on some commands).
- The API payload key is `gpus` (a list of profile type strings), matching the `pyvss` parameter name.
- All VM creation paths (template, clone, clib, shell, image, spec) accept the GPU profiles in the same list-based payload format.
- The `from-file` command (which loads a YAML/JSON spec file) does not need a `--gpu-profile` option because users can include GPU profiles directly in the file spec; it will pass them through to the API automatically.
