class ContractReview:

    def evaluate(self, requirements, delivery):
        return {
            "status": "Review Required",
            "requirements": requirements,
            "delivery": delivery
        }

if __name__ == "__main__":
    review = ContractReview()

    result = review.evaluate(
        "Build landing page",
        "Landing page delivered"
    )

    print(result)
