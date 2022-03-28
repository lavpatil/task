def param_val = ""
    stage("Build"){
        def build_var = build job: 'Build'
        param_val = build_var.rawBuild.getEnvironment()[<Variable name you defined>]
     }
    stage("Run") {
         build job: 'Run', parameters: [string(name: '<param>', value: param_val)
    }
