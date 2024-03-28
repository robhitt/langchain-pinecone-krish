[
    Document(
        page_content='Portal\nBE\n-\nRunbook\nPurpose\nhttp://oas-portal-api.ps.svc.kube.la.taboolasyndication.com/docs\n(Swagger)\nThis\nrunbook\nprovides\nstep-by-step\ninstructions\nfor\ntroubleshooting\nor\nrestarting\nthe\nPortal\nFront\nBackend\nweb\napp\nin\nthe\nevent\nof\nan\noutage\nor\nlive\nsite\nissue.\nPrerequisites\nAccess\nto\nTaboola\nJenkins-CI\nAccess\nto\nArtifactory\nDeployment\n(Production)\nJenkins\n-\nBuild\nhttps://ci.taboolasyndication.com/job/oas-portal-api/job/production\n(or\nsearch:\noas-por tal-api/pr oduction\n)\n●\nThis\njob\nwill\nbuild\nthe\nlatest\nproduction\nbranch\nimage\nand\npush\nit\nto\nArtifactory\n●\nClick\nBuild\nNow\nW\n●\nWait\nfor\nthe\nbuild\nto\ncycle\nthrough\nall\nthe\nsteps\nsuccessfully\n○\nIf\nthere\nare\nerrors\nin\nthe\nbuild,\nhover\nover\nthe\nbuild\n#,\nselect\nthe\ndropdown\narrow\nand\nchoose\n"Console\nOutput"\nto\ntroubleshoot\nerror\nlogs\nConfirm',
        metadata={"source": "../pdfs/portal-be-runbook.pdf", "page": 0},
    ),
    Document(
        page_content='Output"\nto\ntroubleshoot\nerror\nlogs\nConfirm\nDeployment\nto\nArtifactory\nhttp://artifactory.taboolasyndication.com\n●\nArtifacts\n→\ndocker\n→\ntaboola\n→\noas-portal-api\n→\nMatch\nyour\nbuild\n#\nfrom\nthe\nJenkins\nbuild\njob\nwith\nthe\nbuild\n#\nin\nthe\nArtifactory\nfolder\nto\nconfirm\nbuild\ndeployment\nsucceeded.\nJenkins\n-\nDeploy\nhttps://ci.taboolasyndication.com/job/Helm.Chart.Deploy\n(or\nsearch:\nHelm.Chart.Deploy\n)\n●\nBuild\nWith\nParameters\n○\nCHART_NAME:\noas-portal-api\n■\nNote:\nif\noas-portal-api\nis\nmissing\nfrom\nCHART_NAME,\nrun\nthe\nHelm.Chart.Build\njob\nby\nclicking\nBuild\nwith\nParameters\n,\nthen\nin\nthe',
        metadata={"source": "../pdfs/portal-be-runbook.pdf", "page": 0},
    ),
    Document(
        page_content='USER_PARAMETERS\ntext\nfield\ninput\nCHARTS_FROM_USER=oas-portal-api\nand\nclick\nbuild.\n■\nNavigate\nback\nto\nthe\nHelm.Chart.Deploy\njob\nand\nthe\nCHART_NAME\nshould\nnow\nhave\nthe\noas-portal-api\nvalue\nlisted\n○\nCHART_VERSION:\nLeave\nas\nis\n○\nIMAGE_VERSION:\nSelect\nyour\nrecent\nbuild\n#\n○\nDOMAINS:\nla\n.taboolasyndication.com\n○\nClick\nBuild\n○\nWait\nfor\nBuild\nto\nComplete\n●\nConfirm\nchanges\nare\nlive:\nhttp://oas-portal-api.ps.svc.kube.la.taboolasyndication.com/docs\nin\nincognito.\n○\nYou\nmay\nneed\nto\nreauthenticate\n@\nhttps://authentication.taboola.com\nDeployment\n(Staging)\nJenkins\n-\nBuild\nTBD\nJenkins\n-\nDeploy\nTBD\nDeployment\n(Revert\nto\na\nPrevious\nPortal\nVersion)\nPush\nPrevious\nDisk\nImage\nto\nKubernetes\n●\nhttps://ci.taboolasyndication.com/job/Helm.Chart.Deploy\n●\nClick\n"Build\nWith\nParameters"\n●\nOn\nthe\n"Pipeline',
        metadata={"source": "../pdfs/portal-be-runbook.pdf", "page": 1},
    ),
    Document(
        page_content='Click\n"Build\nWith\nParameters"\n●\nOn\nthe\n"Pipeline\nHelm.Chart.Deploy"\npage\nselect:\n○\nCHART_NAME:\noas-portal-api\n○\nCHART_VERSION:\nLeave\nas\nis\n○\nIMAGE_VERSION:\nSelect\na\nprevious\nbuild\n#\nyou\'d\nlike\nto\ndeploy\n○\nDOMAINS:\nla\n.taboolasyndication.com\n○\nClick\nBuild\n○\nWait\nfor\nBuild\nto\nComplete\n●\nConfirm\nchanges\nare\nlive:\nhttp://oas-portal-api.ps.svc.kube.la.taboolasyndication.com/docs',
        metadata={"source": "../pdfs/portal-be-runbook.pdf", "page": 1},
    ),
    Document(
        page_content="Troubleshooting\n1.\nCheck\nuser\nconnectivity\n○\nVerify\nthe\nTaboola\nVPN\nis\non\nand\ninternet\nconnection\nis\navailable.\n○\nConfirm\nother\nTaboola\nwebsites\nand\nservices\nare\naccessible\nto\ndetermine\nif\nthe\nissue\nis\nspecific\nto\nthe\nPortal\nfrontend.\n2.\nCheck\nif\nthe\nissue\nIs\nonly\nrelated\nto\nlocale/region\n3.\nCheck\nfor\nlive\nsite\nerror\nlogs\n-\n[\nKibana\nPortal\nK8s\nPod\n[oas-portal-api\n]\n4.\nCheck\nfor\nlatency\n/\nheavy\nload\non\nthe\noffstage\nserver?\nGrafana\nBackend\nAPI\n-\nLast\n3\nhrs\n5.\nCheck\nother\nslack\nchannels\nfor\ndowntime\nthat\nmay\nbe\nan\noverall\nTaboola\nissue\nrather\nthan\nPortal\nfrontend\nspecific.\nHere's\na\nstart:\n#downtime\n,\n#data\n,\n#prodit\n,\n#askofficeit\n6.\nLook\nthrough\nthe\nFAQ\nbelow\n7.\nReach\nout\nto\n#keep-portal-on\nif\nunable\nto\nsolve\nthe\nissue.\n8.\nRedeploy\nApplication\n9.\nRollback\nto\nPrevious\nProduction\nBuild\n10.",
        metadata={"source": "../pdfs/portal-be-runbook.pdf", "page": 2},
    ),
    Document(
        page_content="9.\nRollback\nto\nPrevious\nProduction\nBuild\n10.\nOnce\nresolved\nnotify\nthe\n#keep-portal-on\nchannel\nof\nthe\ndowntime\nand\nresolution.\nFAQ\nQ:\nWhere\nis\nthe\nPortal\nrepository?\nA:\nFrontend:\nhttps://git.taboolasyndication.com/projects/PS/repos/oas-portal\nBackend:\nhttps://git.taboolasyndication.com/projects/PS/repos/oas-portal-api/browse\nQ:\nAutoQA\nis\nlagging\nwhen\nscrapping\na\nurl\n(Depricated)\nA:\nSee\nthe\noas-portal-api\nGrafana\npage\nin\nthe\nevent\nthe\nservers\nare\noverwhelmed\n[\nGrafana\n-\nLast\n3\nhrs\n]\nQ:\nAutoQA\n/\nHow\ncan\nI\nmonitor\nAutoQA\nTasks?\nA:\nhttp://oas-crawler-api.ps.svc.kube.la.taboolasyndication.com:7789/queues\nBullMQ\ndepends\non\nRedis\n-\ncould\nbe\na\nroot\ncause\nof\ntasks\nnot\nresolving\nand\ntherefore\nDB\ninserts\nnot\nhappening",
        metadata={"source": "../pdfs/portal-be-runbook.pdf", "page": 2},
    ),
    Document(
        page_content="Unset\nredis:\n{\nhost:\n'oas001.ps.fog.taboolasyndication.com',\nport:\n6379, \n},",
        metadata={"source": "../pdfs/portal-be-runbook.pdf", "page": 3},
    ),
]
