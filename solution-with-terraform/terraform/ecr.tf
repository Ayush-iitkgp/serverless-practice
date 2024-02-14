# Set up the ecr repo

resource "aws_ecr_repository" "greetings_repository" {
  name                 = "solution-terraform"
  force_delete         = true
  image_tag_mutability = "MUTABLE"
}