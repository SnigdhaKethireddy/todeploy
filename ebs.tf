provider "aws" {
  access_key = ""
  secret_key= ""
  region  = "us-east-1"

}

resource "aws_s3_bucket" "b" {
  bucket = "for-practice-aws1"
  acl    = "public-read"
}


resource "aws_elastic_beanstalk_application" "application" {
  name        = "staging"
}
resource "aws_elastic_beanstalk_environment" "environment" {
  name                = "staging-1"
  application         = aws_elastic_beanstalk_application.application.name
  solution_stack_name = "64bit Amazon Linux 2 v3.3.2 running Python 3.8"
setting {
        namespace = "aws:autoscaling:launchconfiguration"
        name      = "IamInstanceProfile"
        value     = "aws-elasticbeanstalk-ec2-role"
      }
}

resource "aws_elastic_beanstalk_application" "application1" {
  name        = "poduction"
}
resource "aws_elastic_beanstalk_environment" "environment1" {
  name                = "production-1"
  application         = aws_elastic_beanstalk_application.application1.name
  solution_stack_name = "64bit Amazon Linux 2 v3.3.2 running Python 3.8"
setting {
        namespace = "aws:autoscaling:launchconfiguration"
        name      = "IamInstanceProfile"
        value     = "aws-elasticbeanstalk-ec2-role"
      }
}








