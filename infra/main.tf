# Deliberately weak Terraform for SecureShip IaC scanning (test fixture, never applied).
resource "aws_s3_bucket" "uploads" {
  bucket = "secureship-test-uploads"
}

resource "aws_security_group" "ssh" {
  name = "allow-ssh-from-anywhere"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
