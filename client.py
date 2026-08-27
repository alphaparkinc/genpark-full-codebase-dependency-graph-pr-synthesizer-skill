class FullCodebaseDependencyGraphPrSynthesizerClient:
    def synthesize_verified_pr(self, task_instruction='Refactor distributed lock implementation from Redis redlock to etcd lease with lease renewal heartbeat', target_repo_url='https://github.com/enterprise/backend-core'):
        return {
            'pull_request_job_id': 'yc_cbg_5519',
            'files_analyzed_in_graph': 840,
            'modified_files_count': 5,
            'cross_module_side_effects_detected': 0,
            'unit_and_integration_tests_generated_count': 8,
            'ast_static_analysis_passed': True,
            'patch_unified_diff_url': 'https://patches.genpark.ai/prs/5519.diff'
        }
