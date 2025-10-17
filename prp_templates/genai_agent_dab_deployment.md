# GenAI Agent Databricks Asset Bundle Deployment - Product Requirement Prompt Template

## Project Information
**Project Name**: `[PROJECT_NAME]`
**Agent Type**: `[AGENT_TYPE - e.g., Multi-Agent Financial Analysis, RAG Chatbot, Code Generation, etc.]`
**Primary Use Case**: `[DESCRIBE_PRIMARY_USE_CASE]`
**Target Audience**: `[TARGET_USERS]`

## Current State Analysis

### Existing Infrastructure
- **Current Databricks Setup**: `[DESCRIBE_CURRENT_SETUP]`
- **Existing Agent Implementation**: `[DESCRIBE_AGENT_ARCHITECTURE]`
- **Data Sources**: `[LIST_DATA_SOURCES_AND_TYPES]`
- **Current Deployment Method**: `[MANUAL/BASIC_AUTOMATION/NONE]`
- **Pain Points**: `[LIST_CURRENT_CHALLENGES]`

### Agent Architecture Overview
- **Agent Framework**: `[LangGraph/LangChain/Custom/Other]`
- **Core Components**: `[LIST_MAIN_COMPONENTS]`
- **LLM Configuration**: `[ENDPOINT_NAME_AND_PROVIDER]`
- **External Integrations**: `[APIS_DATABASES_SERVICES]`
- **State Management**: `[DESCRIBE_STATE_HANDLING]`

## Multi-Stage Deployment Requirements

### 1. Test Stage
**Purpose**: Automated testing and validation of agent functionality

**Requirements**:
- [ ] Unit tests for core agent components
- [ ] Integration tests with external services
- [ ] Performance benchmarking (response time, throughput)
- [ ] Configuration validation
- [ ] Error handling and edge case testing
- [ ] Specific test scenarios: `[LIST_PROJECT_SPECIFIC_TESTS]`

**Success Criteria**:
- [ ] All unit tests pass with >95% coverage
- [ ] Integration tests complete successfully
- [ ] Response time < `[TARGET_RESPONSE_TIME]` seconds
- [ ] Error rate < `[TARGET_ERROR_RATE]`%
- [ ] Custom metrics: `[PROJECT_SPECIFIC_METRICS]`

### 2. Evaluate Stage  
**Purpose**: Quality assessment and performance evaluation

**Requirements**:
- [ ] Response quality evaluation using `[EVALUATION_FRAMEWORK]`
- [ ] Accuracy assessment against ground truth dataset
- [ ] `[DOMAIN_SPECIFIC_METRICS]` validation
- [ ] A/B testing framework for prompt optimization
- [ ] User experience metrics collection
- [ ] Custom evaluation criteria: `[PROJECT_SPECIFIC_EVALUATIONS]`

**Success Criteria**:
- [ ] Response accuracy > `[TARGET_ACCURACY]`%
- [ ] User satisfaction score > `[TARGET_SATISFACTION]`
- [ ] `[DOMAIN_SPECIFIC_THRESHOLD]`
- [ ] Evaluation metrics: `[LIST_KEY_METRICS_AND_THRESHOLDS]`

### 3. Stage Environment
**Purpose**: Pre-production validation and user acceptance testing

**Requirements**:
- [ ] Production-like environment setup
- [ ] Load testing with `[TARGET_CONCURRENT_USERS]` concurrent users  
- [ ] Stress testing for peak usage scenarios
- [ ] Security validation and compliance checks
- [ ] User acceptance testing with `[STAKEHOLDER_GROUPS]`
- [ ] Rollback mechanism testing
- [ ] Environment-specific configurations: `[LIST_STAGING_CONFIGS]`

**Success Criteria**:
- [ ] Handles `[TARGET_LOAD]` requests per minute
- [ ] Zero security vulnerabilities
- [ ] UAT approval from `[APPROVAL_STAKEHOLDERS]`
- [ ] Successful rollback testing
- [ ] Performance under load: `[LOAD_TESTING_CRITERIA]`

### 4. Production Deployment
**Purpose**: Live deployment with monitoring and observability

**Requirements**:
- [ ] Deployment strategy: `[BLUE_GREEN/CANARY/ROLLING]`
- [ ] Model serving endpoint configuration
- [ ] Comprehensive monitoring and alerting
- [ ] Health check implementation
- [ ] Automated rollback triggers
- [ ] Production-specific features: `[LIST_PROD_FEATURES]`

**Success Criteria**:
- [ ] Zero-downtime deployment
- [ ] Health checks pass consistently
- [ ] Monitoring dashboards operational
- [ ] Alert configurations tested
- [ ] SLA compliance: `[DEFINE_SLA_REQUIREMENTS]`

## Databricks Asset Bundle Configuration

### Bundle Structure
```yaml
bundle:
  name: ${var.project_name}
  compute_id: ${var.compute_id}

variables:
  project_name:
    default: "[PROJECT_NAME]"
  workspace_url:
    description: "Databricks workspace URL"
  # Add project-specific variables:
  # [LIST_CUSTOM_VARIABLES]

targets:
  test:
    mode: development
    workspace:
      host: ${var.workspace_url}
    variables:
      experiment_suffix: "-test"
      job_suffix: "-test"
      # Custom test variables:
      # [TEST_SPECIFIC_VARS]
  
  evaluate:
    mode: development  
    workspace:
      host: ${var.workspace_url}
    variables:
      experiment_suffix: "-eval"
      job_suffix: "-eval"
      # Custom evaluation variables:
      # [EVAL_SPECIFIC_VARS]
      
  stage:
    mode: staging
    workspace:
      host: ${var.workspace_url}
    variables:
      experiment_suffix: "-stage" 
      job_suffix: "-stage"
      # Custom staging variables:
      # [STAGE_SPECIFIC_VARS]
      
  prod:
    mode: production
    workspace:
      host: ${var.workspace_url}
    variables:
      experiment_suffix: ""
      job_suffix: ""
      # Custom production variables:
      # [PROD_SPECIFIC_VARS]
```

### Resource Definitions

**MLflow Experiments**:
- Test experiment: `/Shared/[PROJECT_NAME]${var.experiment_suffix}/test`
- Evaluation experiment: `/Shared/[PROJECT_NAME]${var.experiment_suffix}/evaluate`
- Staging experiment: `/Shared/[PROJECT_NAME]${var.experiment_suffix}/staging` 
- Production experiment: `/Shared/[PROJECT_NAME]${var.experiment_suffix}/production`

**Databricks Jobs**:
- `[PROJECT_NAME]_test_job`: Automated testing workflow
- `[PROJECT_NAME]_evaluate_job`: Evaluation and quality assessment
- `[PROJECT_NAME]_stage_job`: Staging deployment and validation
- `[PROJECT_NAME]_deploy_job`: Production deployment

**Additional Resources**:
- `[LIST_ADDITIONAL_RESOURCES - e.g., Model Serving Endpoints, SQL Warehouses, etc.]`

## Implementation Notebooks

### Test Notebook (`src/test_[PROJECT_NAME].py`)
**Purpose**: Comprehensive agent testing
- [ ] Core functionality tests
- [ ] `[AGENT_SPECIFIC_TEST_CASES]`
- [ ] Integration tests with `[EXTERNAL_SERVICES]`
- [ ] Performance benchmarks
- [ ] Configuration validation

### Evaluation Notebook (`src/evaluation_[PROJECT_NAME].py`)  
**Purpose**: Agent quality assessment
- [ ] Response quality evaluation using `[EVALUATION_METHOD]`
- [ ] `[DOMAIN_METRICS]` accuracy testing
- [ ] Comparative analysis against benchmarks
- [ ] A/B testing framework
- [ ] Quality scoring and reporting

### Staging Deployment (`src/deploy_stage_[PROJECT_NAME].py`)
**Purpose**: Pre-production deployment
- [ ] Staging environment setup
- [ ] Load and stress testing
- [ ] User acceptance testing preparation
- [ ] Security and compliance validation
- [ ] Rollback testing

### Production Deployment (`src/deployment_[PROJECT_NAME].py`)
**Purpose**: Production deployment and monitoring
- [ ] `[DEPLOYMENT_STRATEGY]` implementation
- [ ] Health check configuration
- [ ] Monitoring and alerting setup
- [ ] Automated rollback mechanisms
- [ ] Production-specific optimizations

## Configuration Management

### Environment-Specific Configurations
**Files to Create**:
- `configs/test_[PROJECT_NAME].yaml`
- `configs/evaluate_[PROJECT_NAME].yaml`
- `configs/staging_[PROJECT_NAME].yaml`
- `configs/production_[PROJECT_NAME].yaml`

**Configuration Categories**:
```yaml
# Agent Configuration
agent_configs:
  [AGENT_TYPE]:
    # Prompts and behavior
    system_prompt: "[CUSTOMIZE_FOR_PROJECT]"
    # LLM settings
    llm:
      endpoint_name: "[LLM_ENDPOINT]"
      parameters:
        temperature: [VALUE]
        max_tokens: [VALUE]
    # Project-specific settings:
    # [LIST_AGENT_SPECIFIC_CONFIGS]

# Databricks Configuration  
databricks_configs:
  catalog: "[CATALOG_NAME]"
  schema: "[SCHEMA_NAME]"
  workspace_url: "[WORKSPACE_URL]"
  # Data sources:
  # [LIST_DATA_SOURCE_CONFIGS]

# Feature Flags
feature_flags:
  # Enable/disable features by environment:
  # [LIST_FEATURE_FLAGS]

# Deployment Configuration
deployment_config:
  rollout_strategy: "[STRATEGY]"
  health_check_timeout: [TIMEOUT_SECONDS]
  rollback_threshold: [THRESHOLD]
  monitoring_enabled: true
```

## Security and Compliance

### Authentication and Authorization
- [ ] Service principal setup per environment
- [ ] Minimal permission principles
- [ ] Secret management strategy
- [ ] Unity Catalog permissions: `[SPECIFIC_PERMISSIONS_NEEDED]`
- [ ] API authentication for `[EXTERNAL_SERVICES]`

### Compliance Requirements
- [ ] Data privacy compliance: `[REGULATIONS - e.g., GDPR, CCPA]`
- [ ] Industry-specific regulations: `[INDUSTRY_COMPLIANCE]`
- [ ] Security policy enforcement
- [ ] Audit trail implementation
- [ ] Data retention policies

## Monitoring and Observability

### Key Metrics
**Technical Metrics**:
- [ ] Agent response latency (target: `[TARGET_LATENCY]`ms)
- [ ] Request throughput (target: `[TARGET_THROUGHPUT]` req/min)
- [ ] Error rate (target: <`[TARGET_ERROR_RATE]`%)
- [ ] System resource utilization
- [ ] Custom metrics: `[PROJECT_SPECIFIC_TECHNICAL_METRICS]`

**Business Metrics**:
- [ ] `[DOMAIN_ACCURACY]` (target: >`[TARGET_ACCURACY]`%)
- [ ] User satisfaction score (target: >`[TARGET_SATISFACTION]`)
- [ ] Task completion rate (target: >`[TARGET_COMPLETION]`%)
- [ ] Custom business metrics: `[PROJECT_SPECIFIC_BUSINESS_METRICS]`

### Alerting Configuration
- [ ] Performance degradation alerts (>`[LATENCY_THRESHOLD]`ms)
- [ ] Error rate thresholds (>`[ERROR_THRESHOLD]`%)
- [ ] Resource utilization warnings (>`[RESOURCE_THRESHOLD]`%)
- [ ] Security incident notifications
- [ ] Custom alerts: `[PROJECT_SPECIFIC_ALERTS]`

## Success Criteria and KPIs

### Deployment Success Metrics
- [ ] Deployment success rate > `[TARGET_SUCCESS_RATE]`%
- [ ] Mean time to deployment < `[TARGET_DEPLOYMENT_TIME]` minutes
- [ ] Zero-downtime deployments: `[TARGET_UPTIME]`%
- [ ] Rollback success rate > `[TARGET_ROLLBACK_SUCCESS]`%

### Agent Performance KPIs  
- [ ] Response accuracy > `[TARGET_ACCURACY]`%
- [ ] Average response time < `[TARGET_RESPONSE_TIME]` seconds
- [ ] User satisfaction score > `[TARGET_SATISFACTION]`
- [ ] Custom KPIs: `[PROJECT_SPECIFIC_KPIS]`

### Business Impact Metrics
- [ ] `[BUSINESS_METRIC_1]`: `[TARGET_VALUE]`
- [ ] `[BUSINESS_METRIC_2]`: `[TARGET_VALUE]`
- [ ] Cost reduction: `[TARGET_COST_SAVINGS]`%
- [ ] Time savings: `[TARGET_TIME_SAVINGS]`%

## Implementation Timeline

### Phase 1: Foundation (Week `[START_WEEK]`-`[END_WEEK]`)
- [ ] Update databricks.yml with multi-target structure
- [ ] Create environment-specific configuration files
- [ ] Implement basic test and evaluation notebooks
- [ ] Set up initial monitoring and alerting

### Phase 2: Core Deployment Pipeline (Week `[START_WEEK]`-`[END_WEEK]`)
- [ ] Implement staging deployment automation
- [ ] Create production deployment with `[ROLLOUT_STRATEGY]`
- [ ] Set up approval workflows
- [ ] Configure automated testing and validation

### Phase 3: Advanced Features (Week `[START_WEEK]`-`[END_WEEK]`)
- [ ] Implement A/B testing framework
- [ ] Add comprehensive monitoring and observability
- [ ] Create automated rollback mechanisms
- [ ] Enhance security and compliance validation

### Phase 4: Optimization (Week `[START_WEEK]`-`[END_WEEK]`)
- [ ] Performance tuning and optimization
- [ ] Cost optimization strategies
- [ ] Advanced analytics and insights
- [ ] Documentation and knowledge transfer

## Risk Assessment and Mitigation

### Technical Risks
| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|---------|-------------------|
| `[TECHNICAL_RISK_1]` | `[HIGH/MEDIUM/LOW]` | `[HIGH/MEDIUM/LOW]` | `[MITIGATION_PLAN]` |
| `[TECHNICAL_RISK_2]` | `[HIGH/MEDIUM/LOW]` | `[HIGH/MEDIUM/LOW]` | `[MITIGATION_PLAN]` |

### Business Risks  
| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|---------|-------------------|
| `[BUSINESS_RISK_1]` | `[HIGH/MEDIUM/LOW]` | `[HIGH/MEDIUM/LOW]` | `[MITIGATION_PLAN]` |
| `[BUSINESS_RISK_2]` | `[HIGH/MEDIUM/LOW]` | `[HIGH/MEDIUM/LOW]` | `[MITIGATION_PLAN]` |

## Testing Strategy

### Unit Testing
- [ ] Core agent component tests
- [ ] `[COMPONENT_SPECIFIC_TESTS]`
- [ ] Mock external service dependencies
- [ ] Configuration validation tests
- [ ] Target coverage: `[TARGET_COVERAGE]`%

### Integration Testing
- [ ] End-to-end workflow testing
- [ ] External service integration tests
- [ ] Database connectivity and query tests
- [ ] Authentication and authorization tests
- [ ] Cross-environment configuration tests

### Performance Testing
- [ ] Load testing with `[CONCURRENT_USERS]` users
- [ ] Stress testing beyond normal capacity
- [ ] Memory and resource utilization testing
- [ ] Latency testing under various conditions
- [ ] Scalability testing

### Security Testing
- [ ] Authentication bypass testing
- [ ] Authorization boundary testing
- [ ] Input validation and sanitization
- [ ] Secrets and credentials security
- [ ] Network security validation

## Documentation Requirements

### Technical Documentation
- [ ] Architecture overview and design decisions
- [ ] API documentation and usage examples
- [ ] Configuration guide and environment setup
- [ ] Troubleshooting guide and common issues
- [ ] Performance tuning recommendations

### User Documentation
- [ ] User guide and tutorials
- [ ] FAQ and common use cases
- [ ] Best practices and guidelines
- [ ] Training materials for `[STAKEHOLDER_GROUPS]`

### Operational Documentation
- [ ] Deployment procedures and rollback steps
- [ ] Monitoring and alerting runbooks  
- [ ] Incident response procedures
- [ ] Maintenance and update procedures

## Customization Instructions

### Project-Specific Adaptations
1. **Replace all placeholders** marked with `[PLACEHOLDER_NAME]` with project-specific values
2. **Customize agent architecture** sections based on your specific implementation
3. **Adapt success criteria** to match your business requirements
4. **Modify resource definitions** to include project-specific Databricks resources
5. **Update configuration templates** with your agent's specific parameters
6. **Customize monitoring metrics** based on your use case requirements

### Environment-Specific Configurations
1. **Development**: Focus on rapid iteration and debugging capabilities
2. **Testing**: Emphasize comprehensive validation and quality gates
3. **Staging**: Mirror production with reduced scale for final validation
4. **Production**: Optimize for performance, reliability, and monitoring

## Approval Checklist

### Technical Approval
- [ ] Architecture review completed by `[TECHNICAL_REVIEWER]`
- [ ] Security review approved by `[SECURITY_REVIEWER]`  
- [ ] Performance requirements validated
- [ ] Compliance requirements verified
- [ ] Infrastructure capacity confirmed

### Business Approval
- [ ] Business requirements signed off by `[BUSINESS_STAKEHOLDER]`
- [ ] Budget approval for infrastructure costs
- [ ] Timeline approved by project management
- [ ] User acceptance criteria defined
- [ ] Success metrics agreed upon

---

**Template Version**: 1.0
**Created**: [DATE]
**Last Modified**: [DATE]
**Created By**: [AUTHOR]

**Usage Instructions**: 
1. Copy this template for your specific project
2. Fill in all `[PLACEHOLDER]` values with project-specific information
3. Customize sections based on your agent architecture and requirements
4. Review and approve with relevant stakeholders
5. Use as input for the execute-prp command to implement the DAB configuration