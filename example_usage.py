from client import FullCodebaseDependencyGraphPrSynthesizerClient

def main():
    client = FullCodebaseDependencyGraphPrSynthesizerClient()
    res = client.synthesize_verified_pr('Upgrade Pydantic v1 models to Pydantic v2 with custom root validators', 'https://github.com/enterprise/ml-api')
    print('PR Job: ' + res['pull_request_job_id'] + ' (' + str(res['files_analyzed_in_graph']) + ' files in graph)')
    print('Modified Files: ' + str(res['modified_files_count']) + ' | Tests Generated: ' + str(res['unit_and_integration_tests_generated_count']))
    print('Zero Side-Effects: ' + str(res['cross_module_side_effects_detected'] == 0) + ' | Static Analysis: ' + str(res['ast_static_analysis_passed']))
    print('Diff URL: ' + res['patch_unified_diff_url'])

if __name__ == '__main__':
    main()
