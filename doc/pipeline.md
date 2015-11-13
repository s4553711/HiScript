# Pipeline
## Workflow
- clean up workspace
- initialize required work directories
- process app and resources
- run job

## Attributes
- name
- taskId
- task path
- script path
- input path
- out path
- setting

## Method
- read_config
- clean
- processApp
- pj_initialize
- logger

## Setting
```json
{
	"config" : {
		"folder" : ["config_dir", "config_dir/script", "log", "result"],
		"output" : "log/analysis.log"
	},
	"apps" : [
		{
			"name" : "fastqc",
			"attrs" : {
				"source": "/path/to/fastqc",
				"linkTarget": "config_dir/fastqc"
			},
			"param" : {
			    "param1" : "value1"
			}
		},
		{ 
			"name" : "velvet",
			"attrs" : {
				"source": "/opt/app/velve",
				"linkTarget": "config_dir/velvet"
			},
			"param" : {
			    "kmer" : "53"
			}
		}
	],
	"samples" : [{
	    "path" : "input/sample_group1_*.fastq",
	    "alias" : "sample1",
	    "param" : {
	        "velvet_h_category" : "long"
	    }
	},{
	    "path" : "input/sample_group2_*.fastq",
	    "alias" : "sample2",
	    "param" : {
	        "velvet_h_category" : "shortPaired"
	    }	
	}],
	"step" : [{
		"name" : "fastqc",
		"packageName" : "QC",
		"className" : "QC"
	},{
		"name" : "Bwa",
		"packageName" : "Bwa",
		"className" : "Bwa"
	}]
}
```
The global setting of a app is writting in **apps/param**. But if there is sample-specific param, it will put under **samples/param**. 

# Task
## Attributes
- jobId
- jobName
- jobQueue
- script path
- task path
- input path
- ouput path

## Method
- init
- run
- finish
