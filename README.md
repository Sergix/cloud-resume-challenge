# Cloud Resume Challenge

> AWS Edition

[Tutorial](https://cloudresumechallenge.dev/docs/the-challenge/aws/)

## Project Structure

### `aws-sam/`

AWS SAM template and function configuration.

- `visitor_count/`: lambda function
- `events/`: JSON tests for visitor count function
- `tests/`: integration and unit tests for API Gateway and function

### `www/`

S3 bucket static site. Deployed to [cloudresume.sergix.dev](https://cloudresume.sergix.dev)

### `.github/workflows/`

GitHub Actions workflows.

- `sam-pipeline`
  - `pytest` for Lambda function and API Gateway in CloudFormation stack
  - `sam build` / `sam deploy`
- `www`
  - Upload to S3
  - Invalidate CloudFront CDN

## Deployment

### Environment

- `AWS_ACCESS_KEY` from IAM user *Access Key ID*
- `AWS_SECRET_ACCESS_KEY` from IAM user *Secret Access Key*
- `AWS_CLOUDFRONT_ID` from AWS CloudFront distribution ID

### Build/Deploy: AWS SAM

- `aws-sam/ $ sam build`
- `aws-sam/ $ sam deploy`

### Deploy: AWS S3

- `www/ $ aws s3 sync ./ s3://BUCKET --delete`
- `www/ $ aws cloudfront create-invalidation --distribution-id $AWS_CLOUDFRONT_ID --paths '/*'`

## Test: AWS Lambda and API Gateway

- `aws-sam/ $ pytest`
